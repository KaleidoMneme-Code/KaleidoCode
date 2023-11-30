import RPi.GPIO as GPIO
from time import sleep
import sys

sys.path.append("..")
from Thread_Code import Thread



GPIO.setmode(GPIO.BCM)

class Motor:
    global fullstep_sequence
    global halfstep_sequence


    fullstep_sequence = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
    halfstep_sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
                                   [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]

    
    def __init__(self, pin_list, C = 1, thread = None):
        if type(pin_list) != list or len(pin_list) != 4:
            raise TypeError("Pass pin_list as a list with 4 entries!")

        self.pin_list = pin_list
        self.thread = Thread.Create_Thread(thread)
        self.C = C

    def Slow(self, time = .02):
        GPIO.setup(self.pin_list, GPIO.OUT)
        
        while not self.thread.Stopped():
            for i in range(len(halfstep_sequence)):
                GPIO.output(self.pin_list, halfstep_sequence[i * self.C])
                sleep(time)

    def Normal(self, time = .02):
        GPIO.setup(self.pin_list, GPIO.OUT)

        while not self.thread.Stopped():
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[i * self.C])
                sleep(time)

    def Fast(self, time = .01):
        GPIO.setup(self.pin_list, GPIO.OUT)
        
        while not self.thread.Stopped():
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[i * self.C])
                sleep(time)


    def ChangeSpeed(self,speed):
        if speed != "Slow" and speed != "Normal" and speed != "Fast":
            raise NameError("Enter Slow, Normal, or Fast as a string")

        self.thread.Stop()
        sleep(.2)

        if speed == "Slow":
            self.thread.Begin()
            self.Normal()
        elif speed == "Normal":
            self.thread.Begin()
            self.Fast()
        elif speed == "Fast":
            self.thread.Begin()
            self.Slow()
    
        
    def StopMotor(self):
        self.thread.Stop()
        sleep(.2)
        GPIO.output(self.pin_list, 0)

    def CleanUp(self):
        GPIO.cleanup()

