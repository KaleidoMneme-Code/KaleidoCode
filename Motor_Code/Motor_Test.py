import Motor_Control as Motor
import time
import sys

sys.path.append("..")
from Thread_Code import Thread



Motor = Motor.Motor([17,27,22,23], lambda: Motor_Speed_Thread)
Motor_Speed_Thread = Thread.Create_Thread(Motor.ChangeSpeed, args=("Fast",))


try:
    Motor.Normal()

except KeyboardInterrupt:
    Motor.StopMotor()
    Motor.CleanUp()


#def Reverse():
  #  if Clockwise:
 #       Motor.C = -1
  #      Clockwise = False

    #elif not Clockwise:
     #   Motor.C = 1
      #  Clockwise = True

#Clockwise = True

#print(Motor.C)
#Reverse()
#print(Motor.C)

#time.sleep(2)
#Reverse()
#print(Motor.C)
