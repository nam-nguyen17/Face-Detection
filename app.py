import tkinter as tk
from cv2 import cv2
import PIL.Image, PIL.ImageTk
import time
import pygame
from videocapture import VideoCapture
from stopwatch import ElapsedTimeClock



class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok=False
        
        # ---------------------------------------------------------------------------------- #
        #timer
        self.timer=ElapsedTimeClock(self.window)

        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # ------------------------------------------------------------------------------------ #

        #video control buttons
        self.btn_start=tk.Button(self.window, text='START', font=("Arial", 12, "bold"), padx=10, command=self.open_camera)
        self.btn_start.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.btn_stop=tk.Button(self.window, text='STOP', font=("Arial", 12, "bold"), padx=10, command=self.close_camera)
        self.btn_stop.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)


        # Button that lets the user take a snapshot
        self.btn_snapshot=tk.Button(self.window, text="Snapshot", font=("Arial", 12, "bold"), width=30, padx=50, command=lambda:[self.snapshot(), self.play_music()])
        self.btn_snapshot.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=tk.YES)

        # quit button
        self.btn_quit=tk.Button(self.window, text='QUIT', font=("Arial", 12, "bold"), command=quit)
        self.btn_quit.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay=10
        self.update()
        self.window.resizable(0, 0)
        self.window.mainloop()

        # ---------------------------------------------------------------------------------- #

    def snapshot(self):
        # Get a frame from the video source
        ret,frame=self.vid.get_frame()

        if ret:
            cv2.imwrite("image/IMG-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

    pygame.mixer.init()
    def play_music(self):
        pygame.mixer.music.load("sample.mp3")
        pygame.mixer.music.play()

            

    def open_camera(self):
        self.ok = True
        self.timer.start()
        print("Camera opened => Recording")



    def close_camera(self):
        self.ok = False
        self.timer.stop()
        print("Camera closed => Not Recording")

       
    def update(self):

        # Get a frame from the video source
        ret, frame=self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0, image=self.photo, anchor=tk.NW)

            self.window.after(self.delay,self.update)

        # ---------------------------------------------------------------------------------- #

def main():
    # Create a window and pass it to the Application object
    App(tk.Tk(),'Video Recorder')

main()    