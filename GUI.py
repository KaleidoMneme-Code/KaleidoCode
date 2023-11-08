# from LED_Code import LED_Control
# from Motor_Code import Motor_Control
# from Camera_Code import Camera

# import pyshortcuts #pip install pyshortcuts
import tkinter as tk
import time


# Main = Motor_Control.Motor([a1,b1,a2,b2])
# Platform = Motor_Control.Motor([a1,b1,a2,b2])
# Cam = Camera.Camera()

window = tk.Tk()
window.geometry("750x500")
window.title("KaleidoCam") # TO DO: CUSTOMIZE THE TITLE

window.configure(background="black")
# window.resizable(False,False) # Alternative






# Cam_Frame = tk.Frame(window,bg="white", height=375,width=600)
# Cam_Frame.pack(side="top")

# Cam.Preview().pack(anchor="center")






Reverse_Img = tk.PhotoImage(file="KaleidoCode/Icons/Reverse_2.png")
Reverse_Img = Reverse_Img.subsample(2,2)

Reverse_Button = tk.Button(window, image=Reverse_Img, width=100, height= 100)
Reverse_Button.pack(anchor="s",side="left")


Pause_Img = tk.PhotoImage(file="KaleidoCode/Icons/Pause.png")
Pause_Img = Pause_Img.subsample(10,10)

Pause_Button = tk.Button(window, image=Pause_Img, width=100,height=100)
Pause_Button.pack(anchor="s", side="left")


Slow_Img = tk.PhotoImage(file="KaleidoCode/Icons/Slow.png")
Slow_Img = Slow_Img.subsample(1,1)

Slow_Button = tk.Button(window, image=Slow_Img, width=100,height=100, 
                        command=lambda: [Hide(Slow_Button), Show(Normal_Button)])
Slow_Button.pack(anchor="s", side="left")


Normal_Img = tk.PhotoImage(file="KaleidoCode/Icons/Normal.png")
Normal_Img = Normal_Img.subsample(5,5)

Normal_Button = tk.Button(window, image=Normal_Img, width=100, height=100,
                          command=lambda: [Hide(Normal_Button), Show(Fast_Button)])
Normal_Button.pack(anchor="s", side="left")


Fast_Img = tk.PhotoImage(file="KaleidoCode/Icons/Fast.png")
Fast_Img = Fast_Img.subsample(5,5)

Fast_Button = tk.Button(window, image=Fast_Img, width=100, height=100,
                        command=lambda: [Hide(Fast_Button), Show(Slow_Button)])
Fast_Button.pack(anchor="s", side="left")



Photo_Img = tk.PhotoImage(file="KaleidoCode/Icons/Photo_2.png")
Photo_Img = Photo_Img.subsample(5,5)

Photo_Button = tk.Button(window, image=Photo_Img, width=100, height= 100)
Photo_Button.pack(anchor="s", side="right")


Record_Img = tk.PhotoImage(file="KaleidoCode/Icons/Record.png")
Record_Img = Record_Img.subsample(1,1)

Record_Button = tk.Button(window, image=Record_Img, width=100, height= 100,
                          command=lambda: Timer())
Record_Button.pack(anchor="s",side="right")







def Hide(button):
    button.pack_forget()

def Show(button):
    button.pack(anchor="s",side="left")

def Timer():
    # txt = tk.StringVar()
    # txt.set("20")

    # lbl = tk.Label(window, textvariable=txt, font=("calibri",40,""),
                #    foreground="red", background="black")
    # lbl.pack(anchor="s")
    # lbl.place(x=550,y=320)

    Record_Button["state"] = tk.DISABLED

    for i in range(20,0,-1):
        # txt.set(str(i))
        window.update()
        time.sleep(1)

        # if i == 1:
        #     txt.set("")
    
    Record_Button["state"] = tk.NORMAL


def Reverse(Motor):
    pass



Hide(Normal_Button)
Hide(Fast_Button)

window.mainloop()