from picamera2 import Picamera2
import time
import os


    
dir = "/home/pi/Documents"
img_dir = "Images"
vid_dir = "Videos"

vid_path = os.path.join(dir,vid_dir)
img_path = os.path.join(dir,img_dir)


if not os.path.exists(img_path):
    os.mkdir(img_path)
if not os.path.exists(vid_path):
    os.mkdir(vid_path)



