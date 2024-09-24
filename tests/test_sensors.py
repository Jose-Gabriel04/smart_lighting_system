import unittest
from sensors.presence_sensor import PresenceSensor
from sensors.luminosity_sensor import LuminositySensor

class TestPresenceSensor(unittest.TestCase):
    def test_read_value(self):
        # Inicializando o sensor com um pino GPIO fictício (11)
        sensor = PresenceSensor(pin=11)
        value = sensor.read_value()
        self.assertIn(value, [0, 1], "O valor do sensor de presença deve ser 0 ou 1.")

class TestLuminositySensor(unittest.TestCase):
    def test_read_value(self):
        sensor = LuminositySensor()
        value = sensor.read_value()
        self.assertTrue(0 <= value <= 32767, "O valor da luminosidade deve estar entre 0 e 32767.")

if __name__ == '__main__':
    unittest.main()