import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)

class Motor:
    global fullstep_sequence
    global halfstep_sequence


    fullstep_sequence = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
    halfstep_sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
                                   [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]


    def __init__(self, pin_list):
        if type(pin_list) != list or len(pin_list) != 4:
            raise TypeError("Pass pin_list as a list with 4 entries!")

        self.pin_list = pin_list    

    def Slow(self, time = .02, C = 1):
        t = True

        GPIO.setup(self.pin_list, GPIO.OUT)
        
        while t:
            for i in range(len(halfstep_sequence)):
                GPIO.output(self.pin_list, halfstep_sequence[C * i])
                sleep(time)


    def Normal(self, time = .02, C = 1):
        t = True

        GPIO.setup(self.pin_list, GPIO.OUT)

        while t:
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[C * i])
                sleep(time)


    def Fast(self, time = .01, C = 1):
        t = True    

        GPIO.setup(self.pin_list, GPIO.OUT)
        
        while t:
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[C * i])
                sleep(time)


    def ChangeSpeed(self,speed):
        if speed != "Slow" or speed != "Normal" or speed != "Fast":
            raise NameError("Enter Slow, Normal, or Fast as a string")
        
        #self.StopMotor()

        if speed == "Slow":
            self.Normal()
        elif speed == "Normal":
            self.Fast()
        elif speed == "Fast":
            self.Slow()

            
        
    def StopMotor(self):
        t = False
        GPIO.output(self.pin_list, 0)
        GPIO.cleanup()
