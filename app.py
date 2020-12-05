import tkinter as tk 
from cv2 import cv2
import PIL.Image, PIL.ImageTk
import time
import datetime as dt
import pygame
from videocapture import VideoCapture
from timer import ElapsedTimeClock



class App:
    def __init__(self, window, window_title, video_source=0, master=None):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok=False
        self.master = master

        #timer
        self.timer=ElapsedTimeClock(self.window)

        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # --------------------------------------------------------------------------------
        # fm = tk.Frame(master)

        #video control buttons
    
        self.img=tk.PhotoImage(file=r"icon/start.png")
        self.btn_start=tk.Button(self.window, image=self.img,padx=3,pady=2, activebackground='#979797', command=lambda:[self.open_camera(), self.startsound()])
        self.btn_start["border"]="0"
        self.btn_start.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.img1=tk.PhotoImage(file=r"icon/stop.png")
        self.btn_stop=tk.Button(self.window, image=self.img1, padx=3, pady=2,activebackground='#979797', command=self.close_camera)
        self.btn_stop["border"]="0"
        self.btn_stop.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)


        # Button that lets the user take a snapshot
        self.img2=tk.PhotoImage(file=r"icon/snap.png")
        self.btn_snapshot=tk.Button(self.window,image=self.img2,padx=3,pady=2, activebackground='#979797', command=lambda:[self.snapshot(), self.play_music()])
        self.btn_snapshot["border"]="0"
        self.btn_snapshot.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # quit button
        self.img3=tk.PhotoImage(file=r"icon/exit.png")
        self.btn_quit=tk.Button(self.window, text='QUIT',image=self.img3,padx=3, pady=2,activebackground='#979797', command=self.quit)
        self.btn_quit["border"]="0"
        self.btn_quit.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay=10
        self.update()
        self.window.resizable(0, 0)
        self.window.mainloop()


    def snapshot(self):
        # Get a frame from the video source
        ret,frame=self.vid.get_frame()

        if ret:
            cv2.imwrite("image/IMG-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

    pygame.mixer.init()
    def play_music(self):
        pygame.mixer.music.load("sample.mp3")
        pygame.mixer.music.play()
    pygame.mixer.init()
    def startsound(self):
         pygame.mixer.music.load("startsound.mp3")
         pygame.mixer.music.play()

    def open_camera(self):
        self.ok = True
        self.timer.start()
        print("camera opened => Recording")



    def close_camera(self):
        self.ok = False
        self.timer.stop()
        print("camera closed => Not Recording")

       
    def update(self):

        # Get a frame from the video source
        ret, frame=self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0, image=self.photo, anchor=tk.NW)
        
            self.window.after(self.delay,self.update)
    def quit(self):
        self.window.destroy()

def main():
    # Create a window and pass it to the Application object
    App(tk.Tk(),'Video Recorder')

main()    