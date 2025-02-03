import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube, Playlist
import os

# Function to download a single YouTube video
def download_video():
    url = url_entry.get()
    path = filedialog.askdirectory()

    if not url or not path:
        messagebox.showerror("Error", "Please enter a URL and select a download folder.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# Function to download a playlist
def download_playlist():
    url = url_entry.get()
    path = filedialog.askdirectory()

    if not url or not path:
        messagebox.showerror("Error", "Please enter a playlist URL and select a download folder.")
        return

    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=path)
        messagebox.showinfo("Success", "Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download playlist: {str(e)}")

# GUI setup
app = tk.Tk()
app.title("YouTube Video & Playlist Downloader")
app.geometry("500x250")

# URL Label and Entry
url_label = tk.Label(app, text="Enter YouTube Video/Playlist URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=60)
url_entry.pack(pady=5)

# Download Buttons
video_button = tk.Button(app, text="Download Video", command=download_video, bg="green", fg="white")
video_button.pack(pady=10)

playlist_button = tk.Button(app, text="Download Playlist", command=download_playlist, bg="blue", fg="white")
playlist_button.pack(pady=5)

# Run the GUI
app.mainloop()