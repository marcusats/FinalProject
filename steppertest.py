

print ("Program Started")

import RPi.GPIO as GPIO
import Motor_control
from Bipolar_Stepper_Motor_Class import Bipolar_Stepper_Motor
import time
from numpy import pi, sin, cos, sqrt, arccos, arcsin



GPIO.setmode(GPIO.BOARD)


motor1=Bipolar_Stepper_Motor(8,10,12,16)
motor2=Bipolar_Stepper_Motor(18,22,24,26)
clark=0

try:
    while clark < 17:
        direction = 1;
        steps = 32;
        motor1.move(direction,steps,0.01)
        #motor2.move(direction,steps,0.01)
        clark= clark + 1
    while clark > 1:
        direction = -1;
        steps = 32;
#         motor1.move(direction,steps,0.01)
        motor2.move(direction,steps,0.01)
        clark= clark - 1
    while clark < 17:
        direction = -1;
        steps = 32;
        motor1.move(direction,steps,0.01)
        #motor2.move(direction,steps,0.01)
        clark= clark + 1
    while clark > 1:
        direction = 1;
        steps = 32;
#         motor1.move(direction,steps,0.01)
        motor2.move(direction,steps,0.01)
        clark= clark - 1
        
        

except KeyboardInterrupt:
    GPIO.cleanup()
