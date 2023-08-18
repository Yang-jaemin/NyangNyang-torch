import random

class DataLoader:
    def __init__(self, dataset, batch_size=1, shuffle=False):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.indices = list(range(len(dataset))) 

    def __iter__(self):
        if self.shuffle:
            random.shuffle(self.indices)

        for start_idx in range(0, len(self.dataset), self.batch_size):
            end_idx = min(start_idx + self.batch_size, len(self.dataset))
            yield [self.dataset[idx] for idx in self.indices[start_idx:end_idx]]  # 제너레이터

    def __len__(self):
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size