import rasterio
import numpy as np
import cv2
import pandas as pd
from skimage.feature import graycomatrix, graycoprops
from skimage.filters import sobel
import argparse
import random
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,    help="path to input dataset")
ap.add_argument("-o", "--output_dir", required=True,    help="path to output dataset")
#ap.add_argument("-m", "--model", required=True,    help="path to output model")
#ap.add_argument("-p", "--plot", type=str, default="plot.png",    help="path to output loss/accuracy plot")
args = vars(ap.parse_args())

# tif file path:  D:\ML_Hackathon\villages_training_dataset\NADALA_28996_ORTHO.tif

tif_path = args["dataset"]
output_dir = args["output_dir"]
image_path = tif_path
tile_size = 512
print("tif file path",tif_path )

def extract_features(tif_path):

    # Read TIFF image
    with rasterio.open(tif_path) as src:
        img = src.read(1)   # Read first band

    # Normalize image
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

    features = {}

    # ---------- Statistical Features ----------
    features["mean"] = np.mean(img)
    features["std"] = np.std(img)
    features["min"] = np.min(img)
    features["max"] = np.max(img)

    # ---------- Edge Features ----------
    edges = sobel(img)
    features["edge_mean"] = np.mean(edges)
    features["edge_std"] = np.std(edges)

    # ---------- Texture Features (GLCM) ----------
    glcm = graycomatrix(img,
                        distances=[1],
                        angles=[0],
                        levels=256,
                        symmetric=True,
                        normed=True)

    features["contrast"] = graycoprops(glcm, 'contrast')[0,0]
    features["correlation"] = graycoprops(glcm, 'correlation')[0,0]
    features["energy"] = graycoprops(glcm, 'energy')[0,0]
    features["homogeneity"] = graycoprops(glcm, 'homogeneity')[0,0]

    # ---------- Shape / Contour Features ----------
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        features["area"] = cv2.contourArea(cnt)
        features["perimeter"] = cv2.arcLength(cnt, True)
    else:
        features["area"] = 0
        features["perimeter"] = 0

    return features

def tile_orthophoto(image_path, output_dir):
    print("Inside title_ortho function------------")
    with rasterio.open(image_path) as src:
        img = src.read([1,2,3])
        img = img.transpose(1,2,0)

    h, w, _ = img.shape

    os.makedirs(output_dir, exist_ok=True)

    count = 0

    for y in range(0, h, tile_size):
        for x in range(0, w, tile_size):

            tile = img[y:y+tile_size, x:x+tile_size]

            if tile.shape[0] != tile_size or tile.shape[1] != tile_size:
                continue

            cv2.imwrite(f"{output_dir}/tile_{count}.png", tile)
            count += 1
    
    print("Outside title_ortho function------------")
    
def main():
    #features = extract_features(tif_path)
    #df = pd.DataFrame([features])
    #print(df)
    
    tile_orthophoto(tif_path, output_dir)

if __name__ == "__main__":
    main()

# Example usage
#features = extract_features("image.tif")

#df = pd.DataFrame([features])
#print(df)