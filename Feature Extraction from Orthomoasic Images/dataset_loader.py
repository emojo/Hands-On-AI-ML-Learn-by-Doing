import torch
from torch.utils.data import Dataset
import rasterio
import os
import numpy as np

class DroneDataset(Dataset):

    def __init__(self, image_dir, mask_dir):

        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.images = os.listdir(image_dir)

    def __len__(self):

        return len(self.images)

    def __getitem__(self, idx):

        img_path = os.path.join(self.image_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.images[idx])

        with rasterio.open(img_path) as src:
            image = src.read([1,2,3])

        with rasterio.open(mask_path) as src:
            mask = src.read(1)

        image = torch.tensor(image).float()
        mask = torch.tensor(mask).long()

        return image, mask