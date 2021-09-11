import os
import numpy as np
import torch
from config import conf

class Mydataset(torch.utils.data.Dataset):
    def __init__(self, x):
        self.x = x

    def __getitem__(self, index):
        return self.x[index]

    def __len__(self):
        return self.x.shape[0]

def load_dataset(path):
    x = []
    dataset_path = path
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            data = np.load(os.path.join(root, file))
            x.append(data)
    x = np.stack(x)
    return x


def get_dataloader(path):
    x = load_dataset(path)
    #mean = 0.2528974
    #std = 0.27297965

    mean = 0.2528974
    std = 0.27297965
    x = (x - mean) / std
    set = Mydataset(x)
    loader = torch.utils.data.DataLoader(set, batch_size=1, shuffle=False)
    return loader