import tkinter
import customtkinter
import pygame
from PIL import Image,ImageTk
from threading import *
import time
import math
import os


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

is_paused = False


root = customtkinter.CTk()
root.title("Groovify")
root.geometry('400x480')

pygame.mixer.init()

list_of_songs = [
    r"W:\A.I\GroovifyMusicPlayer\music\Sunflower.mp3",
    r"W:\A.I\GroovifyMusicPlayer\music\Say_So.mp3",
    r"W:\A.I\GroovifyMusicPlayer\music\Resonance.ogg"
]

list_of_covers = [
    r"W:\A.I\GroovifyMusicPlayer\img\8e29535aa9736adb61ec89d47f59ea5e.jpg",
    r"W:\A.I\GroovifyMusicPlayer\img\b7f7295a118ea87d76727464e5255447.jpg",
    r"W:\A.I\GroovifyMusicPlayer\img\0b7456398fc637799f00743bce550e43.jpg"

]

n = 0

# ---------------- ALBUM + TITLE ---------------------

cover_label = None
title_label = None

def get_album_cover(song_name, index):
    global cover_label, title_label

    # Remove old widgets
    if cover_label:
        cover_label.destroy()
    if title_label:
        title_label.destroy()

    # Load image
    img = Image.open(list_of_covers[index])
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)

    cover_label = tkinter.Label(root, image=img)
    cover_label.image = img  # keep reference
    cover_label.place(relx=.19, rely=.06)

    # Show clean title
    song_clean = os.path.basename(song_name)
    song_clean = song_clean.replace(".mp3","").replace(".ogg","")

    title_label = tkinter.Label(root, text=song_clean, bg='#222222', fg='white')
    font=("Poppins", 28, "bold")
    title_label.place(relx=.5, rely=.93, anchor="center")


# ---------------- PROGRESS BAR ---------------------

def progress():
    audio = pygame.mixer.Sound(list_of_songs[n])
    song_len = audio.get_length()

    for i in range(int(song_len * 3)):
        time.sleep(0.3)
        progressbar.set(pygame.mixer.music.get_pos() / 100000)

def threading_progress():
    Thread(target=progress, daemon=True).start()

# ---------------- MUSIC CONTROL ---------------------

def play_music():
    global n

    if n >= len(list_of_songs):
        n = 0

    song = list_of_songs[n]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)

    get_album_cover(song, n)
    threading_progress()

    n += 1

def skip_forward():
    play_music()

def skip_backward():
    global n
    n -= 2
    if n < 0:
        n = len(list_of_songs) - 1
    play_music()

def volume(value):
    pygame.mixer.music.set_volume(value)

def pause_music():
    global is_paused

    if pygame.mixer.music.get_busy():     # music is playing
        if not is_paused:
            pygame.mixer.music.pause()
            pause_button.configure(text="Resume")
            is_paused = True
        else:
            pygame.mixer.music.unpause()
            pause_button.configure(text="Pause")
            is_paused = False



# ---------------- UI BUTTONS -------------------------

play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_backward, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#6703fc', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

pause_button = customtkinter.CTkButton(master=root, text='Pause', command=pause_music)
pause_button.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)


root.mainloop()
