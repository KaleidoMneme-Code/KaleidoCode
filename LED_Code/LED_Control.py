import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def ConstantOn(self):
        GPIO.output(self.pin, 1)

    def PWM(self, freq, dc):
        global pwm

        pwm = GPIO.PWM(self.pin, freq)
        pwm.start(dc)

    def ChangeFrequency(self, freq):
        pwm.ChangeFrequency(freq)

    def ChangeDutyCycle(self, dc):
        pwm.ChangeDutyCycle(dc)

    def StopLED(self):
        pwm.stop()
        GPIO.output(self.pin, 0)
        GPIO.cleanup()

