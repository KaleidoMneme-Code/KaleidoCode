# def Reverse():
#     global Clockwise
#     if Clockwise:
#         Clockwise = False

# Clockwise = True
# print(Clockwise)
# Reverse()
# print(Clockwise)

class Fake:

    def __init__(self, C=1):
        self.set_C(C)

    def set_C(self,new_C):
        self.C = lambda x: new_C * x
        print(new_C)
        print(self.C)

    def addition(self):
        return self.C + 1
    
    def multiplication(self):
        return self.C * 2

    def getlist(self):
        l = [1,2,3,4,5]
        a = []
        for i in range(len(l)):
            a.append(l[self.C(i)])
        return a

test = Fake()
print(test.getlist())
test.set_C(-1)
print(test.getlist())
# print(test.addition())
# print(test.multiplication())







# import random
# import tkinter as tk
#from tkinter import tix
# from Camera_Code import Camera
# import cv2
# from PIL import Image,ImageTk

# window = tk.Tk()
# window.geometry("400x300")
#window.configure(background="black")

# frame = tk.Frame(window)
# frame.pack()

# label = tk.Label(frame, width=200, height=200)
# label.pack()

# cap = cv2.VideoCapture(0)

# def update_frame():
#     ret,frame=cap.read()
#     print(ret,frame)
#     if ret:
#         print("Hello")
#         frame = cv2.resize(frame,(200,200))
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(img)
#         imgtk = ImageTk.PhotoImage(image=img)
#         label.imgtk = imgtk
#         label.configure(image=imgtk)
#     window.after(10,update_frame)



#tip = tix.Balloon(window)

# def Close():
#     print("HI")
#     window.destroy()

# Button1 = tk.Button(window,  width=10, height=5)
# Button1.pack(anchor="se", side="right")

#tip.bind_widget(Button1, balloonmsg="Welcome! This is Button 1!")

# Button2 = tk.Button(window,  width=10, height=5, fg="red", bg="red")
# Button2.pack(anchor="sw", side="left")



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

# update_frame()

# window.protocol("WM_DELETE_WINDOW", Close)
# window.mainloop()


# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import os

# width = 1750 #750
# height = 1000 # 500
# widget_width = 175 # 50
# widget_height = widget_width
# Icon_size = QSize(widget_width,widget_height)

# tutorial_app = QApplication([])
# tutorial_window = QWidget()

# tutorial_window.setWindowTitle("Tutorial")
# tutorial_window.setGeometry(500,200,width,height)
# tutorial_window.setFixedSize(width,height)

# frame = QFrame(tutorial_window)

# YES = QPushButton("Yes",parent=frame)
# NO = QPushButton("No", parent=frame)
# Question = QLabel("Would you like a tutorial?", parent=frame)

# YES.setGeometry(100,175,3*widget_width,widget_height)
# NO.setGeometry(260,175,3*widget_width,widget_height)

# Question.setGeometry(125,50,300,100)
# Question.setStyleSheet("font-size: 10pt; font-weight: bold")

# YES.clicked.connect(lambda: Open_Tutorial())
# NO.clicked.connect(lambda: Close_Tutorial())

# def Open_Tutorial():
#     os.startfile(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Tutorial.txt")
#     tutorial_window.close()

# def Close_Tutorial():
#     tutorial_window.close()

# tutorial_window.show()
# tutorial_app.exec()



# Clockwise = True
# Recording = False

# app = QApplication([])
# window = QWidget()

# frame = QFrame(window)

# window.setGeometry(500,200,width,height)
# window.setFixedSize(width,height)
# window.setWindowTitle("Dummy Window")
# # window.setWindowFlag(Qt.WindowCloseButtonHint, False)
# window.setWindowFlags(window.windowFlags() | Qt.CustomizeWindowHint)
# window.setWindowFlags(window.windowFlags() & ~Qt.WindowCloseButtonHint) 
# window.setWindowIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Observatory.png"))


# Reverse = QPushButton("",parent=frame)
# Pause = QPushButton("",parent=frame)
# Slow = QPushButton("",parent=frame)
# Normal = QPushButton("",parent=frame)
# Fast = QPushButton("",parent=frame)

# Photo = QPushButton("",parent=frame)
# Record = QPushButton("",parent=frame)

# BorderBottom = QLabel("", parent=frame)
# BorderBottom.setGeometry(1.35*widget_width, height-widget_height-.52*widget_height, width-2.7*widget_width,.52*widget_height)
# BorderBottom.setPixmap(QPixmap(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Upper_Border.png"))
# BorderBottom.setScaledContents(True)

# BorderLeft = QLabel("", parent=frame)
# BorderLeft.setGeometry(0, 0,1.35*widget_width, height-widget_height)
# BorderLeft.setPixmap(QPixmap(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Left_Border.png"))
# BorderLeft.setScaledContents(True)

# BorderRight = QLabel("", parent=frame)
# BorderRight.setGeometry(width-1.35*widget_width, 0,1.35*widget_width, height-widget_height)
# BorderRight.setPixmap(QPixmap(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Right_Border.png"))
# BorderRight.setScaledContents(True)

# ButtonBorder = QLabel("KaleidoSatory™", parent=frame)
# ButtonBorder.setGeometry(3*widget_width,height-widget_height,width-5*widget_width,widget_height)
# ButtonBorder.setPixmap(QPixmap(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Lower_Border.png"))
# ButtonBorder.setScaledContents(True)

# Exit = QPushButton("Exit",parent=frame)
# Exit.setGeometry(width-widget_width,0,widget_width,.25*widget_height)
# Exit.setStyleSheet("background-color: black; color: darkRed; font-size: 30pt; font-weight: bold")

# Reverse.setGeometry(0*widget_width,height-widget_height,widget_width,widget_height)
# Pause.setGeometry(1*widget_width,height-widget_height,widget_width,widget_height)
# Slow.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)
# Normal.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)
# Fast.setGeometry(2*widget_width,height-widget_height,widget_width,widget_height)

# Photo.setGeometry(width-2*widget_width,height-widget_height,widget_width,widget_height)
# Record.setGeometry(width-widget_width,height-widget_height,widget_width,widget_height)

# Reverse.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Reverse_2.png"))
# Reverse.setIconSize(Icon_size)
# Pause.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Pause.png"))
# Pause.setIconSize(Icon_size)

# Slow.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Slow.png"))
# Slow.setIconSize(Icon_size)
# Normal.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Normal.png"))
# Normal.setIconSize(Icon_size)
# Fast.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Fast.png"))
# Fast.setIconSize(Icon_size)

# Photo.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Photo_2.png"))
# Photo.setIconSize(Icon_size)
# Record.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Record.png"))
# Record.setIconSize(Icon_size)

# Slow.clicked.connect(lambda: [Hide(Slow), Show(Normal)])
# Normal.clicked.connect(lambda: [Hide(Normal), Show(Fast)])
# Fast.clicked.connect(lambda: [Hide(Fast), Show(Slow)])

# Reverse.clicked.connect(lambda: [Reverse_Motor()])
# Record.clicked.connect(lambda: [Get_Video()])
# Exit.clicked.connect(lambda: [Close()])


# def Reverse_Motor():
#     global Clockwise

#     Reverse.setEnabled(False)

#     if Clockwise:
#         Reverse.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Reverse_Reverse.png"))
#         Reverse.setIconSize(Icon_size)
#         Clockwise = False


#     elif not Clockwise:
#         Reverse.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Reverse_2.png"))
#         Reverse.setIconSize(Icon_size)
#         Clockwise = True

#     Reverse.setEnabled(True)

# def Get_Video():
#     global Recording
    
#     if not Recording:
#         Recording = True
#         Record.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Recording.png"))
#         Record.setIconSize(Icon_size)
#     else:
#         Recording = False
#         Record.setIcon(QIcon(r"C:\Users\Eric\Desktop\PHYS 351\KaleidoCode\Icons\Record.png"))
#         Record.setIconSize(Icon_size)


# def Hide(button):
#     button.hide()

# def Show(button):
#     button.show()

# def Close():
#     window.close()

# Normal.hide()
# Fast.hide()

# window.show()
# app.exec()
