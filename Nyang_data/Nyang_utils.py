import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from typing import List, Tuple
import numpy as np


def Nyang_split(root_dir: str, classes: List[str], ratios: Tuple[float, float, float] = (0.8, 0.1, 0.1)) -> Tuple[List[Tuple[str, List[int]]], List[Tuple[str, List[int]]], List[Tuple[str, List[int]]]]:
    """
    root_dir: 데이터셋의 루트 디렉토리
    ratios: train, valid, test 데이터셋의 분리 비율
    
    반환값:
    - train_dataset, valid_dataset, test_dataset: 각각의 데이터셋 객체
    -> Tuple[List[Tuple[str, List[int]]], List[Tuple[str, List[int]]], List[Tuple[str, List[int]]]]
    -> 3개의 요소를 포함하는 Tuple을 나타냅니다.
    -> 각 요소는 Tuple[str, List[int]] 을 포함하는 List 입니다.
    -> 이 List의 각 요소는 str(image path)과 List(one-hot-incoding)를 포함하는 Tuple입니다.
    -> 이미지 경로(str)와 해당 이미지의 원-핫 인코딩된 레이블(List[int])을 포함하는 튜플의 리스트를 3개 포함하는 튜플을 나타냅니다.
    -> 이 3개의 리스트는 각각 train, valid, test 데이터셋을 나타낼 수 있습니다.
    """
    all_data = []
    all_labels = []
    
    # 원-핫 인코딩 딕셔너리 초기화
    label_to_onehot = {}

    # 각 클래스에 대해
    for i, cls in enumerate(classes):
        # 원-핫 벡터 초기화
        onehot_vector = []
        
        # 원-핫 벡터 생성
        for j in range(len(classes)):
            if i == j:
                onehot_vector.append(1)
            else:
                onehot_vector.append(0)
        
        # 딕셔너리에 원-핫 벡터 저장
        label_to_onehot[cls] = onehot_vector
        
    
    for label in classes:
        class_dir = os.path.join(root_dir, label)
        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            all_data.append(image_path)
            all_labels.append(label_to_onehot[label])
    
    combined = list(zip(all_data, all_labels))
    random.shuffle(combined)
    
    train_size = int(ratios[0] * len(combined))
    valid_size = int(ratios[1] * len(combined))
    
    train_data = combined[:train_size]
    valid_data = combined[train_size:train_size + valid_size]
    test_data = combined[train_size + valid_size:]
    
    return train_data, valid_data, test_data



def Nyang_images_grid(images: List[np.ndarray], labels: List[List[int]], classes: List[str], nrows: int, ncols: int) -> None:
    """
    
    - 이미지들과 레이블을 그리드 형태로 시각화합니다.
    - one hot incoding을 풀어서 class name을 보여줍니다.
    - augmentation 적용을 확인 해볼 수 있습니다.
    
    """
    fig, axs = plt.subplots(nrows, ncols, figsize=(15, 15))
    axs = axs.ravel()
    
    for i in range(nrows * ncols):
        if i < len(images):
            index = labels[i].index(1) # 원 핫 인코딩 풀어주기
            class_name = classes[index]
            axs[i].imshow(images[i])  # 이미 np.array 형태의 이미지를 직접 imshow에 전달
            axs[i].set_title(class_name)
            axs[i].axis('off')
        else:
            axs[i].remove()  # 빈 서브플롯 제거