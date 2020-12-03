from tkinter import *
import pygame


pygame.mixer.init()
def play_music():
    pygame.mixer.music.load("sample.mp3")
    pygame.mixer.music.play()

root = Tk()
Button(root, text="Play music", command=play_music).pack()
root.mainloop()