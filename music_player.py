import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.root.config(bg="#111111")

        pygame.mixer.init()

        self.current_track = 0
        self.music_files = []
        self.is_playing = False
        self.paused = False

        self.left_frame = tk.Frame(self.root, bg="#111111")
        self.left_frame.pack(side=tk.LEFT, padx=30, pady=30)

        self.right_frame = tk.Frame(self.root, bg="#111111")
        self.right_frame.pack(side=tk.RIGHT, padx=30, pady=30)

        self.play_button = tk.Button(self.left_frame, text="Play", command=self.play_music, width=10, bg="#00CC88", fg="#FFFFFF")
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.left_frame, text="Pause", command=self.pause_music, width=10, bg="#00CC88", fg="#FFFFFF")
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.left_frame, text="Stop", command=self.stop_music, width=10, bg="#00CC88", fg="#FFFFFF")
        self.stop_button.pack(pady=10)

        self.next_button = tk.Button(self.left_frame, text="Next", command=self.next_track, width=10, bg="#00CC88", fg="#FFFFFF")
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(self.left_frame, text="Previous", command=self.prev_track, width=10, bg="#00CC88", fg="#FFFFFF")
        self.prev_button.pack(pady=10) 

        self.load_button = tk.Button(self.right_frame, text="Load Folder", command=self.load_folder, width=20, bg="#5555CC", fg="#FFFFFF")
        self.load_button.pack(pady=10)

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.music_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp3')]
            if self.music_files:
                self.current_track = 0
                messagebox.showinfo("Folder Loaded", f"{len(self.music_files)} tracks loaded.")
            else:
                messagebox.showwarning("No Files", "No .mp3 files found in the selected folder.")

    def play_music(self):
        if not self.music_files:
            messagebox.showwarning("No Files", "No music files loaded.")
            return
        if not self.is_playing or self.paused:
            pygame.mixer.music.load(self.music_files[self.current_track])
            pygame.mixer.music.play()
            self.is_playing = True
            self.paused = False
            self.update_title()

    def pause_music(self):
        if self.is_playing:
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
            else:
                pygame.mixer.music.unpause()
                self.paused = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.stop_music = False
        self.update_title()

    def next_track(self):
        if self.music_files:
            self.current_track = (self.current_track + 1) % len(self.music_files)
            self.is_playing = False
            self.play_music()

    def prev_track(self):
        if self.music_files:
            self.current_track = (self.current_track - 1) % len(self.music_files)
            self.is_playing = False
            self.play_music()

    def update_title(self):
        self.root.title(f"Music Player - Playing: {os.path.basename(self.music_files[self.current_track])}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
