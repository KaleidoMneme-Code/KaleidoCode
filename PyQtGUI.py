from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Motor_Code import Motor_Control
from Camera_Code import Camera
# from LED_Code import LED_Control2
from Thread_Code import Thread
from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
import time

Clockwise = True
Recording = False

Main_Motor = Motor_Control.Motor([17,27,22,23], lambda: Motor_Speed_Thread)
# Sub_Motor = Motor_Control.Motor([1,1,1,1], lambda: Platform_Motor_Thread) #a1,b1,a2,b2
# LED = LED_Control2.LED(thread=lambda: LED_Thread)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())
picam2.configure(picam2.create_video_configuration(main={"size": (1280, 720)}))

Motor_Speed_Thread = Thread.Create_Thread(Main_Motor.ChangeSpeed, args=("Fast",))
# Platform_Motor_Thread = Thread.Create_Thread(Sub_Motor.Slow, args=())
# Platform_Motor_Thread.start()
# LED_Thread = Thread.Create_Thread(LED.ConstantOn, args=())
# LED_Thread.start()

width = 1750
height = 1000
widget_width = 175
widget_height = widget_width
Icon_size = QSize(widget_width,widget_height)


app = QApplication([])

window = QWidget()
window.setWindowTitle("KaleidoSatory")
window.setGeometry(500,200,width,height)
window.setFixedSize(width,height)
window.setWindowFlag(Qt.WindowCloseButtonHint, False)

frame = QFrame(window)

qpicamera2 = QGlPicamera2(picam2, width=width - 2*(1.35*widget_width), height=height-widget_height-.5*widget_height, keep_ar=True,parent=frame)
qpicamera2.move(1.35*widget_width,0)
qpicamera2.done_signal.connect(lambda: capture_done)

Reverse = QPushButton("",parent=frame)
Pause = QPushButton("",parent=frame)
Slow = QPushButton("",parent=frame)
Normal = QPushButton("",parent=frame)
Fast = QPushButton("",parent=frame)

Photo = QPushButton("",parent=frame)
Record = QPushButton("",parent=frame)

BorderBottom = QLabel("", parent=frame)
BorderBottom.setGeometry(0, height-widget_height-.5*widget_height, width,.52*widget_height)
BorderBottom.setStyleSheet("background-color: black")

BorderLeft = QLabel("", parent=frame)
BorderLeft.setGeometry(0, 0,1.35*widget_width, height-widget_height)
BorderLeft.setStyleSheet("background-color: black")

BorderRight = QLabel("", parent=frame)
BorderRight.setGeometry(width-1.35*widget_width, 0,1.35*widget_width, height-widget_height)
BorderRight.setStyleSheet("background-color: black")

ButtonBorder = QLabel("KaleidoCam", parent=frame)
ButtonBorder.setGeometry(3*widget_width,height-widget_height,width-5*widget_width,widget_height)
ButtonBorder.setStyleSheet("background-color: black; color: white; font-size: 75pt; font-weight: bold")
ButtonBorder.setAlignment(Qt.AlignmentFlag.AlignCenter)

Exit = QPushButton("Exit",parent=frame)
Exit.setGeometry(width-widget_width,0,widget_width,.25*widget_height)
Exit.setStyleSheet("background-color: black; color: darkRed; font-size: 30pt; font-weight: bold")

Reverse.setGeometry(0*widget_width,height-widget_height,widget_width,widget_height)
Pause.setGeometry(1*widget_width,height-widget_height,widget_width,widget_height)
Slow.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)
Normal.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)
Fast.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)

Photo.setGeometry(width-widget_width,height-widget_height,widget_width,widget_height)
Record.setGeometry(width-2*widget_width,height-widget_height,widget_width,widget_height)

Reverse.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Reverse_2.png"))
Reverse.setIconSize(Icon_size)
Pause.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Pause.png"))
Pause.setIconSize(Icon_size)

Slow.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Slow.png"))
Slow.setIconSize(Icon_size)
Normal.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Normal.png"))
Normal.setIconSize(Icon_size)
Fast.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Fast.png"))
Fast.setIconSize(Icon_size)

Photo.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Photo_2.png"))
Photo.setIconSize(Icon_size)
Record.setIcon(QIcon("/home/pi/Documents/KaleidoCode/Icons/Record.png"))
Record.setIconSize(Icon_size)


Reverse.clicked.connect(lambda: [Reverse_Motor()])
Pause.clicked.connect(lambda: [Pause_Motor()])


Slow.clicked.connect(lambda: [Hide(Slow), Show(Normal), Speed(Normal,"Slow")])
Normal.clicked.connect(lambda: [Hide(Normal), Show(Fast), Speed(Fast,"Normal")])
Fast.clicked.connect(lambda: [Hide(Fast), Show(Slow), Speed(Slow,"Fast")])

Record.clicked.connect(lambda: [Get_Video()])
Photo.clicked.connect(lambda: Get_Picture())

Exit.clicked.connect(lambda: [Close()])


def Hide(button):
    button.hide()

def Show(button):
    button.show()


def Reverse_Motor():
    global Clockwise

    Reverse.setEnabled(False)
    Motor_Speed_Thread_CurrentStop = False
    Motor_Next_Speed_Thread_CurrentStop = False

    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
        Motor_Speed_Thread_CurrentStop = True
    elif lambda: Motor_Next_Speed_Thread.is_alive():
        lambda: Motor_Next_Speed_Thread.Stop()
        Motor_Next_Speed_Thread_CurrentStop = True

    if Clockwise:
        time.sleep(.2)
        Main_Motor.C = -1
        Clockwise = False

        if Motor_Speed_Thread_CurrentStop:
            Motor_Speed_Thread.Begin()
        elif Motor_Next_Speed_Thread_CurrentStop:
            Motor_Next_Speed_Thread.Begin()


    elif not Clockwise:
        time.sleep(.2)
        Main_Motor.C = 1
        Clockwise = True

        if Motor_Speed_Thread_CurrentStop:
            Motor_Speed_Thread.Begin()
        elif Motor_Next_Speed_Thread_CurrentStop:
            Motor_Next_Speed_Thread.Begin()

    time.sleep(.8)
    Reverse.setEnabled(True)


def Pause_Motor():
    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif Motor_Next_Speed_Thread.is_alive():
        Motor_Next_Speed_Thread.Stop()

    Stop_Thread = Thread.Create_Thread(Main_Motor.StopMotor, args=())

    Stop_Thread.start()
    time.sleep(.1)
    Stop_Thread.Stop()


def Speed(button, speed):
    global Motor_Next_Speed_Thread
    
    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif lambda: Motor_Next_Speed_Thread.is_alive():
        lambda: Motor_Next_Speed_Thread.Stop()


    button.setEnabled(False)
    Motor_Next_Speed_Thread = Thread.Create_Thread(Main_Motor.ChangeSpeed, args=(speed,))
    Motor_Next_Speed_Thread.Begin()
    Motor_Next_Speed_Thread.start()
    time.sleep(.3)
    button.setEnabled(True)


def Get_Picture():
  Photo.setEnabled(False)
  
  cfg = picam2.create_still_configuration()
  picam2.switch_mode_and_capture_file(cfg, "/home/pi/Documents/Images/" + str(time.asctime()) + ".jpg", signal_function=qpicamera2.signal_done)
  
  time.sleep(2)
  Photo.setEnabled(True)

def Get_Video():
    global Recording
    
    if not Recording:
        encoder = H264Encoder(10000000)
        output = FileOutput("/home/pi/Documents/Videos/" + str(time.asctime()) + ".h264")
        picam2.start_encoder(encoder, output)
        Recording = True
    else:
        picam2.stop_encoder()
        Recording = False
        # ADD DIFFERENT PHOTO AT LEAST
    

def Record_Timer():
    Record.setEnabled(False)

    for i in range(183,0,-1):
        time.sleep(.1)

    Record.setEnabled(True)


def capture_done(job):
  result = picam2.wait(job)
  Photo.setEnabled(True)

def Close():
    if lambda: Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif lambda: Motor_Next_Speed_Thread.is_alive():
        Motor_Next_Speed_Thread.Stop()
    elif lambda: Platform_Motor_Thread.is_alive():
        Platform_Motor_Thread.Stop()
    elif lambda: LED_Thread.is_alive():
        LED_Thread.Stop()

    Main_Motor.CleanUp()
    #Sub_Motor.CleanUp()
    #LED.StopLED()
    window.close()

Normal.hide()
Fast.hide()

picam2.start()
window.show()
Motor_Speed_Thread.start()
app.exec()

