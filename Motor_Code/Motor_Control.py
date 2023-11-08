import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Motor:
    global fullstep_sequence
    global halfstep_sequence
    global c

    c = 1

    fullstep_sequence = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
    halfstep_sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
                                   [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]


    def __init__(self, pin_list):
        GPIO.mode(GPIO.BCM)

        if type(pin_list) != list or len(pin_list) != 4:
            raise TypeError("Pass pin_list as a list with 4 entries!")

        GPIO.setup(pin_list, GPIO.OUT)
    

    def Slow(self, time = .02, CounterClockwise = False):
        t = True

        if CounterClockwise == True:
            c = -1

        while t:
            for i in range(len(halfstep_sequence)):
                GPIO.output(self.pin_list, halfstep_sequence[c * i])
                sleep(time)


    def Normal(self, time = .02, CounterClockwise = False):
        t = True

        if CounterClockwise == True:
            c = -1

        while t:
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[c * i])
                sleep(time)


    def Fast(self, time = .01, CounterClockwise = False):
        t = True    
        
        if CounterClockwise == True:
            c = -1

        while t:
            for i in range(len(fullstep_sequence)):
                GPIO.output(self.pin_list, fullstep_sequence[c * i])
                sleep(time)


    def StopMotor(self):
        t = False
        GPIO.output(self.pin_list, 0)
        GPIO.cleanup()
