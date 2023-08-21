import albumentations as A
from albumentations.core.composition import Compose
from typing import Tuple

def Nyang_transforms() -> Tuple[Compose, Compose]:
    train_transform = A.Compose([
        #A.Resize(128, 128),
        #A.RandomCrop(5, 5),
        A.VerticalFlip(p=1.0),
        #A.RandomBrightnessContrast(p=0.2),
        #A.Normalize(mean=[0.5], std=[0.5])
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    valid_transform = A.Compose([
        # A.Resize(128, 128),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        #A.Normalize(mean=[0.5], std=[0.5])
    ])
    
    test_transform = A.Compose([
        #A.Resize(128, 128),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        #A.Normalize(mean=[0.5], std=[0.5])
    ])

    return train_transform, valid_transform, test_transform