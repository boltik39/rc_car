from utils.ConfigData import ConfigData
import RPi.GPIO as GPIO


class Motor:
    __IN_1 = int(ConfigData().get_from_config('motor_pin1'))
    __IN_2 = int(ConfigData().get_from_config('motor_pin2'))
    __FREQUENCY = int(ConfigData().get_from_config('motor_frequency'))

    def __init__(self, in_1: int = __IN_1, in_2: int = __IN_2, frequency: int = __FREQUENCY):
        self._in_1 = in_1
        self._in_2 = in_2
        GPIO.setup(self._in_1, GPIO.OUT)
        GPIO.setup(self._in_2, GPIO.OUT)
        self._in_1_pwm = GPIO.PWM(self._in_1, frequency)
        self._in_2_pwm = GPIO.PWM(self._in_2, frequency)

    def go(self, speed: int):
        print(f"[INFO] Get speed {speed}")
        if abs(speed) <= 100:
            if speed > 0:
                self._in_1_pwm.start(abs(speed))
                GPIO.output(self._in_2, GPIO.LOW)
            elif speed < 0:
                GPIO.output(self._in_1, GPIO.LOW)
                self._in_2_pwm.start(abs(speed))
            else:
                GPIO.output(self._in_1, GPIO.LOW)
                GPIO.output(self._in_2, GPIO.LOW)
        else:
            print(f"[ERROR] wrong speed value {speed}. It must be in [-100, 100]")

    def braking(self):
        print("[INFO] Start braking")
        GPIO.output(self._in_1, GPIO.HIGH)
        GPIO.output(self._in_2, GPIO.HIGH)
