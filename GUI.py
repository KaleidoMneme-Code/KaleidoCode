# from LED_Code import LED_Control
# from LED_Code import LED_Control2
from Motor_Code import Motor_Control
# from Camera_Code import Camera
from Thread_Code import Thread
import tkinter as tk
import tkinter.tix as tix
import time

Clockwise = True

Main_Motor = Motor_Control.Motor([17,27,22,23], lambda: Motor_Speed_Thread)  # a1,b1,a2,b2
# Sub_Motor = Motor_Control.Motor([1,1,1,1], lambda: Platform_Motor_Thread) #a1,b1,a2,b2
# Cam = Camera.Camera()


Motor_Speed_Thread = Thread.Create_Thread(Main_Motor.ChangeSpeed, args=("Fast",))
Motor_Speed_Thread.start()

# Platform_Motor_Thread = Thread.Create_Thread(Sub_Motor.Slow, args=())
# Platform_Motor_Thread.start()

window = tk.Tk()
window.geometry("1750x1000")
window.title("KaleidoCam")

window.configure(background="black")
window.resizable(False,False)

# tip = tix.Balloon(window)

# Cam_Frame = tk.Frame(window,bg="white", height=375,width=600)
# Cam_Frame.pack(side="top")

# Cam.Preview().pack(anchor="n") # Test this
# If not, check https://gist.github.com/kcranley1/3bd43a3c6aeb3ac0804e


Reverse_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Reverse_2.png")
# Reverse_Img = Reverse_Img.subsample(9,9)
# Reverse_Img = Reverse_Img.zoom(7,7)

Reverse_Button = tk.Button(window, image=Reverse_Img, width=175, height=175,
                           command=lambda: [Reverse()])
Reverse_Button.pack(anchor="sw", side="left")
#tip.bind_widget(Reverse_Button, balloonmsg="Press this button to reverse the direction!")


Pause_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Pause.png")
# Pause_Img = Pause_Img.subsample(1024,1024)
# Pause_Img = Pause_Img.zoom(175,175)

Pause_Button = tk.Button(window, image=Pause_Img, width=175, height=175,
                         command= lambda: [Pause()])
Pause_Button.pack(anchor="sw", side="left")
#tip.bind_widget(Pause_Button, balloonmsg="Press this button to pause the Kaleidoscope!")

Slow_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Slow.png")
# Slow_Img = Slow_Img.subsample(44,44)
# Slow_Img = Slow_Img.zoom(35,35)

Slow_Button = tk.Button(window, image=Slow_Img, width=175, height=175, 
                        command=lambda: [Hide(Slow_Button), Show(Normal_Button), 
                                        Speed(Normal_Button,"Slow")])
Slow_Button.pack(anchor="sw", side="left")
#tip.bind_widget(Slow_Button, balloonmsg = "Press this button to go a slow speed!")

Normal_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Normal.png")
# Normal_Img = Normal_Img.subsample(512,512)
# Normal_Img = Normal_Img.zoom(175,175)

Normal_Button = tk.Button(window, image=Normal_Img, width=175, height=175,
                          command=lambda: [Hide(Normal_Button), Show(Fast_Button),
                                           Speed(Fast_Button,"Normal")])
Normal_Button.pack(anchor="sw", side="left")
#tip.bind_widget(Normal_Button, balloonmsg = "Press this button to go a normal speed!")

Fast_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Fast.png")
# Fast_Img = Fast_Img.subsample(24,24)
# Fast_Img = Fast_Img.zoom(7,7)

Fast_Button = tk.Button(window, image=Fast_Img, width=175, height=175,
                        command=lambda: [Hide(Fast_Button), Show(Slow_Button),
                                         Speed(Slow_Button,"Fast")])
Fast_Button.pack(anchor="sw", side="left")
#tip.bind_widget(Fast_Button, balloonmsg = "Press this button to go a fast speed!")


Photo_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Photo_2.png")
# Photo_Img = Photo_Img.subsample(512,512)
# Photo_Img = Photo_Img.zoom(175,175)

Photo_Button = tk.Button(window, image=Photo_Img, width=175, height=175)
Photo_Button.pack(anchor="se", side="right")
#tip.bind_widget(Photo_Button, balloonmsg = "Take a picture!")

Record_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Record.png")
# Record_Img = Record_Img.subsample(312,208)
# Record_Img = Record_Img.zoom(175,175)

Record_Button = tk.Button(window, image=Record_Img, width=175, height=175,
                          command=lambda: Timer())
Record_Button.pack(anchor="se", side="right")
#tip.bind_widget(Record_Button, balloonmsg = "Record a video!")



def Hide(button):
    button.pack_forget()

def Show(button):
    button.pack(anchor="sw", side="left")

def Timer():
    Record_Button["state"] = tk.DISABLED

    for i in range(183,0,-1):
        window.update()
        time.sleep(.1)

    Record_Button["state"] = tk.NORMAL

def Reverse():
    global Clockwise

    if Clockwise:
        Main_Motor.C = -1
        Clockwise = False

    elif not Clockwise:
        Main_Motor.C = 1
        Clockwise = True

def Speed(button, speed):
    global Motor_Next_Speed_Thread

    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif lambda: Motor_Next_Speed_Thread.is_alive():
        lambda: Motor_Next_Speed_Thread.Stop()

    button["state"] = tk.DISABLED
    Motor_Next_Speed_Thread = Thread.Create_Thread(Main_Motor.ChangeSpeed, args=(speed,))
    Motor_Next_Speed_Thread.Begin()
    Motor_Next_Speed_Thread.start()
    time.sleep(.3)
    button["state"] = tk.NORMAL

def Pause():
    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif Motor_Next_Speed_Thread.is_alive():
        Motor_Next_Speed_Thread.Stop()

    Stop_Thread = Thread.Create_Thread(Main_Motor.StopMotor, args=())

    Stop_Thread.start()
    time.sleep(.1)
    Stop_Thread.Stop()


def Close(Escape):
    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif Motor_Next_Speed_Thread.is_alive():
        Motor_Next_Speed_Thread.Stop()
    # elif Platform_Motor_Thread.is_alive():
    #     Platform_Motor_Thread.Stop()

    Main_Motor.CleanUp()
    # Sub_Motor.CleanUp()
    #Cam.StopCamera()
    window.destroy()



Hide(Normal_Button)
Hide(Fast_Button)

window.bind("<Escape>", Close)
#window.protocol("WM_DELETE_WINDOW", Close)
window.mainloop()
