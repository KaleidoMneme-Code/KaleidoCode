import RPi.GPIO as GPIO
from time import sleep
import random
import sys

sys.path.append("..")
from Thread_Code import Thread

class LED:
    global f
    global duty

    f = 1000
    duty = 0
    
    def __init__(self, Color1=13, Color2=16, Color3=26, thread=None):
        GPIO.setmode(GPIO.BCM)

        pin_list = [Color1, Color2, Color3]
        self.pin_list = pin_list

        GPIO.setup(pin_list, GPIO.OUT)

        self.pwm_Color1 = GPIO.PWM(Color1, f)
        self.pwm_Color2 = GPIO.PWM (Color2, f)
        self.pwm_Color3 = GPIO.PWM(Color3, f)

        self.pwm_Color1.start(duty)
        self.pwm_Color2.start(duty)
        self.pwm_Color3.start(duty)

        self.thread = Thread.Create_Thread(thread)

    def ConstantOn(self):
        while not self.thread.Stopped():
            r1,r2,r3 = (random.randrange(25,100,5) for x in range(3))
            
            for dc in range (r1,-1,-5):
                self.pwm_Color1.ChangeDutyCycle(dc)
                sleep (.1)
            
            for dc in range (0,r2+1,5):
                self.pwm_Color3.ChangeDutyCycle(dc)
                sleep (.1)

            for dc in range (r3,-1,-5):
                self.pwm_Color2.ChangeDutyCycle(dc)
                sleep (.1)

            for dc in range (0,r1+1,5):
                self.pwm_Color1.ChangeDutyCycle(dc)
                sleep (.1)
        
            for dc in range (r2,-1,-5):
                self.pwm_Color3.ChangeDutyCycle(dc)
                sleep (.1)

            for dc in range (0,r3+1,5):
                self.pwm_Color2.ChangeDutyCycle(dc)
                sleep (.1)
            
    def StopLED(self):
        self.thread.Stop()
        self.pwm_Color1.stop()
        self.pwm_Color2.stop()
        self.pwm_Color3.stop()
    
        GPIO.output(self.pin_list,0)
        GPIO.cleanup()
        
