import Motor_Control as Motor
from time import sleep

Motor = Motor.Motor([17,27,22,23])

try:
    Motor.Fast()

except KeyboardInterrupt:
    Motor.StopMotor()

