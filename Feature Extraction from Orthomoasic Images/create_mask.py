import geopandas as gpd
import rasterio
import os
from rasterio.features import rasterize

#label_file = "D:\/ML_Hackathon\/Merged_Lables_using_Qgis\/labels.shp"
label_file = "D:\/ML_Hackathon\/Merged Labels using Python\/labels.shp"
image_dir = "D:\/ML_Hackathon\/villages_training_dataset\/dataset\/images"
mask_dir =   "D:\/ML_Hackathon\/villages_training_dataset\/dataset\/masks1"

#label_file = "../data/labels.shp"
#image_dir = "../dataset/images"
#mask_dir = "../dataset/masks"



os.makedirs(mask_dir, exist_ok=True)

labels = gpd.read_file(label_file)

for file in os.listdir(image_dir):

    image_path = os.path.join(image_dir, file)
    print("Labels Class_id:", labels.class_id," and ", labels.class_name, "Labels--Geometry-->",labels.geometry)

    with rasterio.open(image_path) as src:

        mask = rasterize(
            [(geom, value) for geom, value in zip(labels.geometry, labels.class_id)],
            out_shape=(src.height, src.width),
            transform=src.transform,
            fill=0,
            dtype="uint8"
        )

        mask_path = os.path.join(mask_dir, file)

        with rasterio.open(
                mask_path,
                "w",
                driver="GTiff",
                height=src.height,
                width=src.width,
                count=1,
                dtype="uint8",
                transform=src.transform
        ) as dst:

            dst.write(mask, 1)

print("Mask generation completed")

#----------------------------------------
'''
import rasterio
import numpy as np
from rasterio.plot import show

# 1. Open the input file
#input_tif = 'input_image.tif'
input_tif = "D:\/ML_Hackathon\/villages_training_dataset\/NADALA_28996_ORTHO.tif"
#output_labels = 'labels.tif'
output_labels =   "D:\/ML_Hackathon\/villages_training_dataset\/dataset\/masks\/labels.tif"

with rasterio.open(input_tif) as src:
    # Read the data (assuming 3 bands: R, G, B)
    image = src.read()
    profile = src.profile
    
    # 2. Create labels (Multi-class Example: 0: Background, 1: Veg, 2: Water)
    # Replace this with your specific classification logic
    labels = np.zeros((src.height, src.width), dtype=np.uint8)
    
    # Simple thresholding example
    # Assuming NIR band is band 4, and Red is 3
    # normalized_diff = (NIR - Red) / (NIR + Red)
    
    # Define classes based on thresholding
    # Class 1: Vegetation (e.g., NDVI > 0.3)
    labels[(image[3] > 1000)] = 1  
    
    # Class 2: Water (e.g., Blue band > 1500)
    labels[(image[0] > 1500)] = 2  

    # 3. Update metadata for the new label file
    profile.update(
        dtype=rasterio.uint8,
        count=1,  # Single band for label
        nodata=0  # Set no data value
    )

    # 4. Write the label file
    with rasterio.open(output_labels, 'w', **profile) as dst:
        dst.write(labels, 1)

print(f"Labeled raster saved to {output_labels}")
'''