from cv2 import cv2
from paser import CommandLineParser
import numpy as np



class VideoCapture:  
    def __init__(self, video_source=0):
        
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Command Line Parser
        
        args=CommandLineParser().args

        
        #create videowriter

        # 1. Video Type
        VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            #'mp4': cv2.VideoWriter_fourcc(*'H264'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }

        self.fourcc=VIDEO_TYPE[args.type[0]]

        # 2. Video Dimension
        STD_DIMENSIONS = {
            '480p': (640, 480),
            # '720p': (900, 500),
            '1080p': (1920, 1080),
            '4k': (3840, 2160),
        }
        res = STD_DIMENSIONS[args.res[0]]
        print(args.name, self.fourcc, res)
        self.out = cv2.VideoWriter(args.name[0]+'.'+args.type[0], self.fourcc, 14, res)

        #set video sourec width and height
        self.vid.set(3, res[0])
        self.vid.set(4, res[1])

        # Get video source width and height
        self.width, self.height = res
      


    # To get frames
    def get_frame(self):
        if self.vid.isOpened():
            ret, img = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to cv2.COLOR_RGB2BGR
                return (ret, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

            else:
                return (ret, img)
        else:
            return (ret, None)


    def write(self,frame):
        self.out.write(frame)       
        

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            self.out.release()
            cv2.destroyAllWindows()


