import torch
from config import conf
class conv_4(torch.nn.Module):
    def __init__(self):
        super(conv_4, self).__init__()

        self._extractor = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),

            torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),

            torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=4),

            torch.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=4)
        )

        self._classifier = torch.nn.Sequential(
            torch.nn.Linear(in_features=2048, out_features=1024),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(in_features=1024, out_features=256),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(in_features=256, out_features=len(conf.class_names)),
            torch.nn.Softmax(dim=1)
        )

    def forward(self, x):
        x = torch.unsqueeze(x, 1)
        x = self._extractor(x)
        x = x.view(x.size(0), x.size(1) * x.size(2) * x.size(3))
        x = self._classifier(x)

        return x

model = conv_4()
model.load_state_dict(torch.load(conf.state_dict_path), strict=False)