class Dataset:
    def __init__(self, data_path, transform=None):
        self.data_path = data_path
        self.data = self.load_data()
        self.transform = transform
    
    def load_data(self):
        pass

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        
        # transform 적용
        if self.transform:
            sample = self.transform(sample)
            
        return sample