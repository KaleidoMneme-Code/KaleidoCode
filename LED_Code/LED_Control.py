import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

f = 1000
duty = 0

Color1 = 13
Color2 = 16
Color3 = 26

pwm_Color1 = GPIO.PWM(Color1, f)
pwm_Color2 = GPIO.PWM (Color2, f)
pwm_Color3 = GPIO.PWM(Color3, f)

pwm_Color1.start(duty)
pwm_Color2.start(duty)
pwm_Color3.start(duty)


while i =  1:
    for dc in range (0,101,5):
        pwm_red.ChangeDutyCycle(dc)
        sleep (.1)

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


GPIO.cleanup()
