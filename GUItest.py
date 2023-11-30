# def Reverse():
#     global Clockwise
#     if Clockwise:
#         Clockwise = False

# Clockwise = True
# print(Clockwise)
# Reverse()
# print(Clockwise)

# class Fake:
#     global l

#     l = [1,2,3,4,5]
#     def __init__(self, C=1):
#         self.C = C

#     def addition(self):
#         return self.C + 1
    
#     def multiplication(self):
#         return self.C * 2

#     def getlist(self):
#         a = []
#         for i in range(len(l)):
#             a.append(l[self.C*i])
#         return a

# test = Fake()
# test.C = -1
# print(test.getlist())
# print(test.addition())
# print(test.multiplication())






import random
import tkinter as tk
#from tkinter import tix
from Camera_Code import Camera
import cv2
from PIL import Image,ImageTk

window = tk.Tk()
window.geometry("400x300")
#window.configure(background="black")

frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, width=200, height=200)
label.pack()

cap = cv2.VideoCapture(0)

def update_frame():
    ret,frame=cap.read()
    print(ret,frame)
    if ret:
        print("Hello")
        frame = cv2.resize(frame,(200,200))
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    window.after(10,update_frame)



#tip = tix.Balloon(window)

def Close():
    print("HI")
    window.destroy()

Button1 = tk.Button(window,  width=10, height=5)
Button1.pack(anchor="se", side="right")

#tip.bind_widget(Button1, balloonmsg="Welcome! This is Button 1!")

Button2 = tk.Button(window,  width=10, height=5, fg="red", bg="red")
Button2.pack(anchor="sw", side="left")



#tip.bind_widget(Button2, balloonmsg="Welcome! This is Button 2!")


#def key_press(e):
 #   ran = random.randint(0,10)
    # print(ran)
  #  if ran > 5:
   #     Button1.pack(anchor="sw", side="left")
    #    Button2.pack(anchor="se", side="right")
    #else:
     #   Button1.pack(anchor="n", side="top")
      #  Button2.pack(anchor="s", side="bottom")

#def key_press2(q):
 #   Button2.pack(anchor="sw", side="left")
  #  Button1.pack(anchor="se", side="right")

#window.bind("<E>W", key_press)
#window.bind("<q>", key_press2)

update_frame()

window.protocol("WM_DELETE_WINDOW", Close)
window.mainloop()



