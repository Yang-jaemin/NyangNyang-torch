import os
from PIL import Image
import numpy as np
from Nyang_dataset import Nyang_Dataset
from Nyang_dataset import NyangNyang_Dataset
from Nyang_dataloader import Nyang_DataLoader
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from typing import List, Tuple
from Nyang_utils import Nyang_split
from Nyang_utils import Nyang_images_grid
from Nyang_transform import Nyang_transforms



def NyangNyang_Dataset_Ready(root_dir: str, classes: List[str], mode: str = "train", batch_size: int = 32, shuffle: bool = True) -> Nyang_DataLoader:
    """
    NyangNyang_Dataset과 Nyang_DataLoader를 합침
    
    Parameters:
    - root_dir: 데이터셋의 경로
    - classes: 데이터셋의 클래스 목록
    - mode: 데이터셋 모드 ("train", "valid", "test")
    - batch_size: 배치
    - shuffle: 데이터 셔플 유무
    
    Returns:
    - data_loader: 준비된 Nyang_DataLoader 객체
    """
    
    # 데이터셋의 변환을 정의합니다.
    train_transform, valid_transform, test_transform = Nyang_transforms()

    # CustomDataset 객체를 생성합니다.
    dataset = NyangNyang_Dataset(root_dir, classes)
    dataset.set_mode("train")
    print("train set:",len(dataset))
    dataset.set_mode("valid")
    print("valid set:",len(dataset))
    dataset.set_mode("test")
    print("test set:",len(dataset))
    
    dataset.set_mode(mode)

    # Nyang_DataLoader 객체를 생성합니다.
    if mode == "train":
        transform = train_transform
    elif mode == "valid":
        transform = valid_transform
    else:
        transform = test_transform

    data_loader = Nyang_DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, transform=transform)
    
    return data_loader