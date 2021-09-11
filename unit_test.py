import unittest
import extract_data as exdt
from config import conf
import manage_data as md

class MyTestCase(unittest.TestCase):
    def test_load_dataset_1(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_1.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_1"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_2(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_2.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_2"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_3(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_3.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_3"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_4(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_4.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_4"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_5(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_5.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_5"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_6(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_6.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_6"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_7(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_7.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_7"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_8(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_8.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_8"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_9(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_9.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_9"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_load_dataset_10(self):
        filename = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_10.txt"
        filepath = "D:\\Phantom\\My\\NeiroMus\\test_data\\x_dataset_10"
        f = open(filename, 'r')
        x = f.read()
        f.close()
        y = str(md.load_dataset(filepath))
        self.assertEqual(True, y == x)

    def test_filter_files_1(self):
        filename = "test.txt"
        self.assertEqual(False, exdt.filter_files(filename))

    def test_filter_files_2(self):
        filename = "test.wav"
        self.assertEqual(True, exdt.filter_files(filename))

    def test_filter_files_3(self):
        filename = "test.mp3"
        self.assertEqual(False, exdt.filter_files(filename))

    def test_filter_files_4(self):
        filename = "test.vwav"
        self.assertEqual(False, exdt.filter_files(filename))

    def test_filter_files_5(self):
        filename = "test.mp4"
        self.assertEqual(False, exdt.filter_files(filename))

    def test_normir_number_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def test_normir_number_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def test_normir_number_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def test_normir_number_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def test_normir_number_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")

    def get_dataloader_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def get_dataloader_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def get_dataloader_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def get_dataloader_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def get_dataloader_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")

    def load_raw_track_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def load_raw_track_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def load_raw_track_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def load_raw_track_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def load_raw_track_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")

    def melspectrogram_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def melspectrogram_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def melspectrogram_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def melspectrogram_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def melspectrogram_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")

    def format_track_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def format_track_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def format_track_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def format_track_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def format_track_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")

    def split_track_1(self):
        num = 4
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0004")

    def split_track_2(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 2) == "02")

    def split_track_3(self):
        num = 5
        self.assertEqual(True, exdt.normir_number(str(num), 4) == "0005")

    def split_track_4(self):
        num = 6
        self.assertEqual(True, exdt.normir_number(str(num), 3) == "006")

    def split_track_5(self):
        num = 2
        self.assertEqual(True, exdt.normir_number(str(num), 1) == "2")



if __name__ == '__main__':
    unittest.main()
