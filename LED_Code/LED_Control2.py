import RPi.GPIO as GPIO
from time import sleep

class LED:
    global f
    global duty

    f = 1000
    duty = 0
    
    def __init__(self, Color1=13, Color2=16, Color3=26):
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

    def ConstantOn(self):
        for dc in range (100,-1,-5):
            self.pwm_Color1.ChangeDutyCycle(dc)
            sleep (.1)
        
        for dc in range (0,101,5):
            self.pwm_Color3.ChangeDutyCycle(dc)
            sleep (.1)

        for dc in range (100,-1,-5):
            self.pwm_Color2.ChangeDutyCycle(dc)
            sleep (.1)

        for dc in range (0,101,5):
            self.pwm_Color1.ChangeDutyCycle(dc)
            sleep (.1)
    
        for dc in range (100,-1,-5):
            self.pwm_Color3.ChangeDutyCycle(dc)
            sleep (.1)

        for dc in range (0,101,5):
            self.pwm_Color2.ChangeDutyCycle(dc)
            sleep (.1)
            
    def StopLED(self):
        self.pwm_Color1.stop()
        self.pwm_Color2.stop()
        self.pwm_Color3.stop()

        GPIO.output(self.pin_list,0)
        GPIO.cleanup()
        