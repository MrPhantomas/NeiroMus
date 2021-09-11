import os
import sys
class Config(object):
    def __init__(self):
        self.track_slice_time = 30000 #ms
        self.sample_rate = 22050 #hz
        self.sample_width = 2 #byte
        self.channels = 1
        self.track_slice_coiff = 0.3
        self.add_zeros = False

        self.n_fft = 1024
        self.hop_length = 512
        self.win_length = 1024
        self.n_mels = 128

        self.class_names = ['JPop', 'Блюз', 'Дабстеп', 'Джаз', 'Диско', 'Индастриал', 'Инди', 'Кантри', 'Классика', 'Панк', 'Регги', 'Техно', 'Транс', 'Хаус', 'ХипХоп']
        self.melspec_resize_lenght = 1024
        self.prepare_path = os.path.abspath(os.path.dirname(sys.argv[0])) + "\\tmp\\prepare"
        self.melspectrogram_path = os.path.abspath(os.path.dirname(sys.argv[0])) + "\\tmp\\melspectrogram"
        self.state_dict_path = os.path.abspath(os.path.dirname(sys.argv[0])) + "\\data_13_102"

conf = Config()
