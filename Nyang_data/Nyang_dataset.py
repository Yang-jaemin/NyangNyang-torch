from abc import ABC, abstractmethod
from typing import Any, Tuple, List
from Nyang_utils import Nyang_split

class Nyang_Dataset(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        pass
    
    @abstractmethod
    def __getitem__(self, idx: int) -> Any:
        pass
    
    
    # 사용자가 custom dataset을 만들게 하기 위해서 dataset class를 추상 클래스로 만듬
    # ABC클래스는 추상클래스의 기본 클래스로 사용됨(상속) -> ABC는 직접 인스턴스화 불가능
    # abstractmethod decorater를 사용해서 추상 메쏘드로 표시 
    
    # 이 글래스를 상속받는 서브클래스가 해당 추상 매쏘드를 구현해야만 인스턴스화가 가능(강제)
    # 데코레이터의 이름을 통해서 의도를 명시할 수 있음
    # 장점 1. 강제성 부여 -> 구현 안하면 인스턴스화가 불가
    # 장점 2. 클래스 구현 가이드 -> 필요한 부분을 빠트리지 않게 ㅇㅇ
    
    # 요약하면, @abstractmethod 데코레이터는 해당 메서드가 반드시 구현되어야 함을 나타내며, 이를 통해 클래스의 설계 의도와 구조를 더 명확하게 표현할 수 있게 함
    

class NyangNyang_Dataset(Nyang_Dataset):
    
    def __init__(self, root_dir, classes, ratios = (0.8, 0.1, 0.1)):
        self.train_data, self.valid_data, self.test_data = Nyang_split(root_dir, classes, ratios)
        self.data = self.train_data  # 기본적으로 train 데이터로 설정
        
    def set_mode(self, mode: str):
        if mode == "train":
            self.data = self.train_data
        elif mode == "valid":
            self.data = self.valid_data
        elif mode == "test":
            self.data = self.test_data
        else:
            raise ValueError("Invalid mode. Choose from ['train', 'valid', 'test']")
        
        return self # method chaining
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx: int) -> Tuple[str, List[int]]:
        image_path, label = self.data[idx]
        return image_path, label 
    
    
    