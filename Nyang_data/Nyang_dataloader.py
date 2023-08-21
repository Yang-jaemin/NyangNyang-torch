from typing import List, Tuple, Iterable
import random
from PIL import Image
import numpy as np

class Nyang_DataLoader:
    def __init__(self, dataset: List[Tuple[str, List[int]]], batch_size: int = 1, shuffle: bool = False, transform = None):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.transform = transform
        self.indexs = list(range(len(dataset)))
         

    def __iter__(self) -> Iterable[Tuple[List[np.ndarray], List[List[int]]]]:
        if self.shuffle:
            random.shuffle(self.indexs)
        for start_idx in range(0, len(self.dataset), self.batch_size):
            end_idx = min(start_idx + self.batch_size, len(self.dataset))
            batch = [self.dataset[idx] for idx in self.indexs[start_idx:end_idx]]
            
            numpy_images = []
            images = [sample[0] for sample in batch]
            labels = [sample[1] for sample in batch]
            
            # transform
            
            for image_path in images:
                image = Image.open(image_path)
                if self.transform:
                    transformed = self.transform(image=np.array(image))
                    numpy_images.append(transformed["image"])  # albumentations은 딕셔너리로 반환
                else:
                    numpy_images.append(np.array(image))

            yield numpy_images, labels  # 제너레이터 쓴 이유 : 배치로 뱉어주고 다음배치는 end_idx부터 시작해야되니까

    def __len__(self) -> int:
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size