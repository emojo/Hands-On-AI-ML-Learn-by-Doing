class Config:
    DATA_IMAGE_PATH =  "D:\/ML_Hackathon\/villages_training_dataset\/NADALA_28996_ORTHO.tif"
    DATA_SHP_PATH = "D:\/ML_Hackathon\/villages_training_dataset\/shp-file\/"
    LABELS_SHP_PATH = "D:\/ML_Hackathon\/villages_training_dataset\/"
    
    DATASET_IMAGE_PATH ="C:\/My_D_Drive\/Customers\/Source_Code\/DataScience_Machine_Learning\/feature_extraction_from_tif\/dataset\/images"
    DATASET_MASK_PATH ="C:\/My_D_Drive\/Customers\/Source_Code\/DataScience_Machine_Learning\/feature_extraction_from_tif\/dataset\/masks"
    
    
    TILE_SIZE = 256
    STRIDE = 256
    EPOCH=2
    
    
    
    MODEL_PATH = "D:\/ML_Hackathon\/model/unet_model.pth"
    
    CLASSES = {
        "rooftop": 1,
        "Road": 2,
        "water": 3,
        "tank": 4
    }