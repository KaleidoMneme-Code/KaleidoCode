import RPi.GPIO as GPIO
from time import sleep

class LED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        f = 1000
        duty = 0

        pwm_Color1 = GPIO.PWM(Color1, f)
        pwm_Color2 = GPIO.PWM (Color2, f)
        pwm_Color3 = GPIO.PWM(Color3, f)

        Color1 = 13
        Color2 = 16
        Color3 = 26

    def ConstantOn(self):
        pwm_Color1.start(duty)
        pwm_Color2.start(duty)
        pwm_Color3.start(duty)

        for dc in range (100,-1,-5):
            pwm_blue.ChangeDutyCycle(dc)
            sleep (.1)
        
        for dc in range (0,101,5):
            pwm_green.ChangeDutyCycle(dc)
            sleep (.1)

        for dc in range (100,-1,-5):
            pwm_red.ChangeDutyCycle(dc)
            sleep (.1)

        for dc in range (0,101,5):
            pwm_blue.ChangeDutyCycle(dc)
            sleep (.1)
    
         for dc in range (100,-1,-5):
            pwm_green.ChangeDutyCycle(dc)
            sleep (.1)
            
    def StopLED(self):
        pwm.stop()
        GPIO.output(Color1, 0)
        GPIO.output(Color2, 0)
        GPIO.output(Color3, 0)
        GPIO.cleanup()
