from utils.ConfigData import ConfigData
import RPi.GPIO as GPIO


class Servo:
    __PIN = int(ConfigData().get_from_config('servo_pin'))
    __FREQUENCY = int(ConfigData().get_from_config('servo_frequency'))

    def __init__(self, servo_pin: int = __PIN, frequency: int = __FREQUENCY):
        self._servo_pin = servo_pin
        GPIO.setup(self._servo_pin, GPIO.OUT)
        self._servo_pin_pwm = GPIO.PWM(self._servo_pin, frequency)
        self._servo_pin_pwm.start(7.5)

    def rotate(self, rotation: float):
        print(f"[INFO] Get rotation {rotation}")
        if (rotation <= 12.5) and (rotation >= 2.5):
            self._servo_pin_pwm.ChangeDutyCycle(rotation)
        else:
            print(f"[ERROR] wrong rotation value {rotation}. It must be in [2.5, 12.5]")
