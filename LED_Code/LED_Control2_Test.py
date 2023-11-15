import LED_Control_2

LED2 = LED_Control_2.LED()

t = True
try:
    while t:
        LED2.ConstantOn()

except KeyboardInterrupt:
    LED2.StopLED()


