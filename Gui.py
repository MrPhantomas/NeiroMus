from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb
from _thread import start_new_thread
import extract_data as extrd
import predictor
from config import conf
import os

def find_track():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("wav and mp3 files", "*.wav;*.mp3"), ("all files", "*.*")))
    print("Open file " + file_path)
    txt.delete(0, END)
    txt.insert(0, file_path)
    text.configure(text="[Жанр] - [вероятность*100]%")
    return

def start_detection():
    # open and convert
    filename = txt.get()
    extrd.extraction(filename)
    #prediction
    genre, probability = predictor.predict()
    print(genre, "-", str(probability)+"%")
    #show prediction
    text.configure(text=(genre + " - " + str(probability)+"%"))
    return

def detect():
    filename = txt.get()
    if not (str(filename).endswith("mp3") or str(filename).endswith("wav")):
        msg = "Неверный файл или путь к файлу"
        mb.showerror("Ошибка", msg)
        return
    if not os.path.isfile(filename):
        msg = "Неверный путь к файлу"
        mb.showerror("Ошибка", msg)
        return
    start_new_thread(start_detection, ())

def show_all_genres():
    print(conf.class_names)
    msg = str(conf.class_names).replace("[", "").replace("]", "")
    mb.showinfo("Классифицируемые жанры", msg)

window = Tk()
window.title("НейроМуз")
window.geometry('300x250')
window.resizable(False, False)
txt = Entry(window, width=41)
txt.grid(column=1, row=0, pady=10)

btn = Button(window, text="Открыть музыкальный файл", command=find_track, width=42, height=3)
btn.grid(column=1, row=1)

btn2 = Button(window, text="Показать классифицрумые жанры", command=show_all_genres, width=42, height=3)
btn2.grid(column=1, row=2)

btn3 = Button(window, text="Запустить распознавание", command=detect, width=42, height=3)
btn3.grid(column=1, row=3)

text = Label(window, text="[Жанр] - [вероятность*100]%")
text.grid(column=1, row=4, pady=10)

window.mainloop()
