from LED_Code import LED_Control
from Motor_Code import Motor_Control
# from Camera_Code import Camera
from Thread_Code import Thread
import tkinter as tk
import time
import threading

Clockwise = True

Main_Motor = Motor_Control.Motor([17,27,22,23], lambda: Motor_Speed_Thread)  # a1,b1,a2,b2
# Sub_Motor = Motor_Control.Motor([a1,b1,a2,b2])
# Cam = Camera.Camera()


#Stop_Thread = Thread.Create_Thread(Main_Motor.StopMotor, args=())

Motor_Speed_Thread = Thread.Create_Thread(Main_Motor.ChangeSpeed, args=("Fast",))
Motor_Speed_Thread.start()

# Platform_Motor_Thread = Thread.Create_Thread(Sub_Motor.Slow, args=())
# Platform_Motor_Thread.start()

window = tk.Tk()
window.geometry("1750x1000")
window.title("KaleidoCam")

window.configure(background="black")
window.resizable(False,False)


# Cam_Frame = tk.Frame(window,bg="white", height=375,width=600)
# Cam_Frame.pack(side="top")

# Cam.Preview().pack(anchor="n") # Test this
# If not, check https://gist.github.com/kcranley1/3bd43a3c6aeb3ac0804e



#Active_Count = tk.Label(window, text="Active Threads: " + str(threading.active_count()),
                        #foreground="white", background="black")
#Active_Count.pack(anchor="nw", side="left")

#Live_Count = tk.Label(window, text="Speed Thread is: " + str(Motor_Speed_Thread.is_alive())
                      #+ ". Stop Thread is " + str(Stop_Thread.is_alive()) + ".",
                       # foreground="white", background="black")
#Live_Count.pack(anchor="nw", side="left")

#Current_Count = tk.Label(window, text="Current thread is " + str(threading.current_thread()) + ".",
                        #foreground="white", background="black")
#Current_Count.pack(anchor="nw", side="left")



Reverse_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Reverse_2.png")
# Reverse_Img = Reverse_Img.subsample(9,9)
# Reverse_Img = Reverse_Img.zoom(7,7)

Reverse_Button = tk.Button(window, image=Reverse_Img, width=175, height=175,
                           command=lambda: [Reverse()])
Reverse_Button.pack(anchor="sw", side="left")


Pause_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Pause.png")
# Pause_Img = Pause_Img.subsample(1024,1024)
# Pause_Img = Pause_Img.zoom(175,175)

Pause_Button = tk.Button(window, image=Pause_Img, width=175, height=175,
                         command= lambda: [Pause()])
Pause_Button.pack(anchor="sw", side="left")


Slow_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Slow.png")
# Slow_Img = Slow_Img.subsample(44,44)
# Slow_Img = Slow_Img.zoom(35,35)

Slow_Button = tk.Button(window, image=Slow_Img, width=175, height=175, 
                        command=lambda: [Hide(Slow_Button), Show(Normal_Button), 
                                        Speed(Normal_Button,"Slow")])
Slow_Button.pack(anchor="sw", side="left")


Normal_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Normal.png")
# Normal_Img = Normal_Img.subsample(512,512)
# Normal_Img = Normal_Img.zoom(175,175)

Normal_Button = tk.Button(window, image=Normal_Img, width=175, height=175,
                          command=lambda: [Hide(Normal_Button), Show(Fast_Button),
                                           Speed(Fast_Button,"Normal")])
Normal_Button.pack(anchor="sw", side="left")


Fast_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Fast.png")
# Fast_Img = Fast_Img.subsample(24,24)
# Fast_Img = Fast_Img.zoom(7,7)

Fast_Button = tk.Button(window, image=Fast_Img, width=175, height=175,
                        command=lambda: [Hide(Fast_Button), Show(Slow_Button),
                                         Speed(Slow_Button,"Fast")])
Fast_Button.pack(anchor="sw", side="left")


Photo_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Photo_2.png")
# Photo_Img = Photo_Img.subsample(512,512)
# Photo_Img = Photo_Img.zoom(175,175)

Photo_Button = tk.Button(window, image=Photo_Img, width=175, height=175)
Photo_Button.pack(anchor="se", side="right")


Record_Img = tk.PhotoImage(file="/home/pi/Documents/KaleidoCode/Icons/Record.png")
# Record_Img = Record_Img.subsample(312,208)
# Record_Img = Record_Img.zoom(175,175)

Record_Button = tk.Button(window, image=Record_Img, width=175, height=175,
                          command=lambda: Timer())
Record_Button.pack(anchor="se", side="right")



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
    if Clockwise:
        Main_Motor.C = -1
        Clockwise = False

    elif not Clockwise:
        Main_Motor.C = 1
        Clockwise = True

def Speed(button, speed):
    global Motor_Next_Speed_Thread

    #Stop_Thread.Stop()
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


def Close():
    if Motor_Speed_Thread.is_alive():
        Motor_Speed_Thread.Stop()
    elif Motor_Next_Speed_Thread.is_alive():
        Motor_Next_Speed_Thread.Stop()

    # Platform_Motor_Thread.Stop()
    Main_Motor.CleanUp()
    # Sub_Motor.CleanUp()
    #LED Classes go here
    window.destroy()



Hide(Normal_Button)
Hide(Fast_Button)


#window.protocol("WM_DELETE_WINDOW", Close()) # REsults in error Motor_Next_Speed_Thread is not defined.
window.mainloop()
