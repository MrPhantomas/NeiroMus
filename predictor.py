from conv_model import model
import torch
from config import conf
import manage_data as md
import numpy
def predict():
    pred = get_prediction()
    j, = numpy.where(pred == max(pred))
    genre = conf.class_names[j[0]]
    probability = round(pred[j[0]], 3) * 100
    itog = dict()
    for i in range(len(conf.class_names)):
        itog[conf.class_names[i]] = str(round(pred[i], 3)*100)+"%"
    print(itog)
    return genre, probability

def get_prediction():
    model.eval()
    dataloader = md.get_dataloader(conf.melspectrogram_path)
    device = torch.device("cpu")
    pred = numpy.zeros(15, dtype=float)
    for batch, (x) in enumerate(dataloader):
        x = x.to(device)
        prediction = model(x)
        pred += prediction.detach().numpy().ravel()/len(dataloader)
    return pred
