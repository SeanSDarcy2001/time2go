from torch.utils.data import Dataset

class eggDataset(Dataset) :
    """Create a PyTorch dataset with extracted features x and labels y"""
    def __init__(self, x, y, transforms = None):
        self.features = x
        self.labels = y
        self.transform = transforms
  
    def __len__(self):
            return len(self.features)


    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx] 
        