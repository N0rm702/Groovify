🎵 Groovify – A Simple & Beautiful Python Music Player

Groovify is a lightweight, modern-looking music player built using Python, Tkinter, CustomTkinter, Pygame, and Pillow. It allows users to play MP3/OGG files with real-time progress tracking, album art display, and intuitive playback controls.
The goal of Groovify is to offer a clean, minimal, and responsive desktop music player experience with easy code customization.

✨ Features

✅ Play / Pause / Skip Controls
Smooth audio playback with next/previous song navigation.

✅ Dynamic Album Art Display
Automatically loads and displays the song’s corresponding album cover.

✅ Song Title Extraction
Displays clean song names by removing file paths and extensions.

✅ Custom UI with CustomTkinter
Modern look with buttons, sliders, and consistent dark theme.

✅ Volume Control Slider
Adjust music volume in real time using a sleek slider.

✅ Progress Bar Animation
Shows real-time music playback position using pygame’s music timer.

🛠️ Tech Stack

Python 3.x

Tkinter – GUI framework

CustomTkinter – Modern, sleek UI components

Pygame Mixer – Audio playback

Pillow (PIL) – Image handling for album covers

Threading – Smooth progress updates without freezing UI

📁 Folder Structure
GroovifyMusicPlayer/
│── main.py            # Main application script
│── music/             # MP3/OGG audio files
│── img/               # Album cover images
└── README.md

🚀 How To Use

Clone the repository

Install the required libraries:

pip install pygame pillow customtkinter


Add your music files to /music

Add album covers to /img

Run the app:

python main.py
