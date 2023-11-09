from picamera import PiCamera #pip install picamera
import time
import os

class Camera:
    global camera
    global l
    camera = PiCamera()
    l = True

    dir = "/home/pi/Documents"
    img_dir = "Images"
    vid_dir = "Videos"

    vid_path = os.path.join(dir,vid_dir)
    img_path = os.path.join(dir,img_dir)


    if not os.path.exists(img_path):
        os.mkdir(img_path)
    if not os.path.exists(vid_path):
        os.mkdir(vid_path)


    def __init__(self):
        pass

    def Get_Picture(self):
        camera.resolution = (2592, 1944)
        camera.capture("/home/pi/Documents/Images/" + str(time.asctime()) + ".jpg")

    def Preview(self):
        camera.resolution = (1920, 1080)
        camera.start_preview(fullscreen=False, window=(100,20,300,400))
        while l:
            time.sleep(1)
        

    def Record(self, t = 20):
        camera.resolution = (1920, 1080)
        camera.start_recording("/home/pi/Documents/Videos/" + str(time.asctime()) + ".h264")
        time.sleep(t)
        camera.stop_recording()

    def StopCamera(self):
        l = False
        camera.stop_preview()
        camera.close()

