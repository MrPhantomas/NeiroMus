import os
import shutil
import librosa
import numpy as np
from config import conf
from pydub import AudioSegment
import math

def melspectrogram(file_name):
    y, sr = librosa.load(file_name, sr=conf.sample_rate)
    S = librosa.stft(y, n_fft=conf.n_fft, hop_length=conf.hop_length, win_length=conf.win_length)
    mel_basis = librosa.filters.mel(sr=conf.sample_rate, n_fft=conf.n_fft, n_mels=conf.n_mels)
    mel_S = np.dot(mel_basis, np.abs(S))
    mel_S = np.log10(1+10*mel_S)
    mel_S = mel_S.T
    return mel_S

def resize_array(array, length=conf.melspec_resize_lenght):
    resize_array = np.zeros((length, array.shape[1]))
    if array.shape[0] >= length:
        resize_array = array[:length]
    else:
        resize_array[:array.shape[0]] = array
    return resize_array

def load_raw_track(filename):
    if filename.endswith(".mp3"):
        track = AudioSegment.from_file(filename, "mp3")
    elif filename.endswith(".wav"):
        track = AudioSegment.from_file(filename, "wav")
    else:
        track = AudioSegment.silent(1000)
    return track

def filter_files(file_name):
    if file_name.find('.wav') != -1:
        return True
    else:
        return False

def format_track(track, channels=conf.channels, sample_rate=conf.sample_rate, sample_width=conf.sample_width):
    track = track.set_channels(channels)
    track = track.set_frame_rate(sample_rate)
    track = track.set_sample_width(sample_width)
    return track

def split_track(track, slice_time=conf.track_slice_time, track_slice_coiff=conf.track_slice_coiff, add_zeros=conf.add_zeros):
    # Чтоб огрызков по 1 сек не было...
    flag = (math.ceil(float(track.duration_seconds * 1000) / float(slice_time))) * slice_time - float(
        track.duration_seconds * 1000) < track_slice_coiff * slice_time

    if (add_zeros and flag):
        need_duration_time = (math.ceil(float(track.duration_seconds * 1000) / float(slice_time))) * slice_time
        need_time = float(need_duration_time) - float(track.duration_seconds * 1000)
        track = track + track.silent(need_time, track.frame_rate)
    else:
        need_duration_time = (math.floor(float(track.duration_seconds * 1000) / float(slice_time))) * slice_time
        track = track[0:need_duration_time]

    slice_count = int(math.ceil(track.duration_seconds * 1000 / slice_time))
    track_slice_list = [track]
    track_slice_list.clear()

    #for i in range(slice_count):
    #    if i % 3 == 0:
    #        tmp_track = track[i * slice_time:(i + 1) * slice_time]
    #        track_slice_list.insert(i, tmp_track)

    for i in range(slice_count):
            tmp_track = track[i * slice_time:(i + 1) * slice_time]
            track_slice_list.insert(i, tmp_track)
    return track_slice_list

def normir_number(str_number, count):
    need_zero = count - len(str_number)
    if (need_zero <= 0): return str_number
    return (str(str("0") * need_zero)) + str_number


def extraction(filename):
    tmp_path = conf.prepare_path.replace(str("\\" + conf.prepare_path.split("\\")[-1]), "")

    if os.path.exists(conf.prepare_path):
        shutil.rmtree(conf.prepare_path)
    if os.path.exists(conf.melspectrogram_path):
        shutil.rmtree(conf.melspectrogram_path)

    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    if not os.path.exists(conf.prepare_path):
        os.mkdir(conf.prepare_path)
    if not os.path.exists(conf.melspectrogram_path):
        os.mkdir(conf.melspectrogram_path)

    track = load_raw_track(filename)
    track = format_track(track)
    track_list = split_track(track)
    index = 0
    for track in track_list:
        split_filename = conf.prepare_path + '\\'  'track_' + normir_number(str(index), 2) + '.wav'
        track.export(split_filename, format='wav')
        index = index + 1

    index = 0
    listdir = os.listdir(conf.prepare_path)
    list_tracks = list(filter(filter_files, listdir))
    for track_name in list_tracks:
        filename = conf.prepare_path + "\\" + track_name
        feature = melspectrogram(filename)
        feature = resize_array(feature)
        num_chunks = feature.shape[0] / conf.n_mels
        data_chuncks = np.split(feature, num_chunks)

        num_chunk = 0
        for idx, i in enumerate(data_chuncks):
            if num_chunk == 2 or num_chunk == 7:
                melspecgram_filename = conf.melspectrogram_path + '\\' + 'melspectrogram_' + normir_number(str(index), 3) + '.npy'
                np.save(melspecgram_filename, i.astype(np.float32))
                index = index + 1
            num_chunk = num_chunk + 1
    return