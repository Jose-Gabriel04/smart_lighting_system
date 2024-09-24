import RPi.GPIO as GPIO
import time

class PresenceSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read_value(self):
        try:
            # Lê o valor do sensor de presença (0 ou 1)
            return GPIO.input(self.pin)
        except Exception as e:
            print(f"Erro na leitura do sensor de presença: {e}")
            return False