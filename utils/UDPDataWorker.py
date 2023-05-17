from models.Motor import Motor
from models.Servo import Servo
import sys
import RPi.GPIO as GPIO


class UDPDataWorker:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self._motor = Motor()
        self._servo = Servo()

    def work_with_data(self, message: str):
        if message[0] == 'm':
            speed = int(message[2:])
            self._motor.go(speed)
        elif message[0] == 's':
            rotation = float(message[2:])
            self._servo.rotate(rotation)
        elif message[0] == 'b':
            self._motor.braking()
        elif message[0] == 'f':
            GPIO.cleanup()
            sys.exit()

    def __del__(self):
        GPIO.cleanup()
