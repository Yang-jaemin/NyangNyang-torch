import random

class Nyang_DataLoader:
    def __init__(self, dataset, batch_size=1, shuffle=False):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.indexs = list(range(len(dataset))) 

    def __iter__(self):
        if self.shuffle:
            random.shuffle(self.indexs)
        for start_idx in range(0, len(self.dataset), self.batch_size):
            end_idx = min(start_idx + self.batch_size, len(self.dataset))
            batch = [self.dataset[idx] for idx in self.indexs[start_idx:end_idx]]

            images = [sample[0] for sample in batch]
            labels = [sample[1] for sample in batch]

            yield images, labels  # 제너레이터 쓴 이유 : 배치로 뱉어주고 다음배치는 end_idx부터 시작해야되니까

    def __len__(self):
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size