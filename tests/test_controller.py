import unittest
from controllers.lighting_controller import LightingController

class TestLightingController(unittest.TestCase):
    def setUp(self):
        # Configurações básicas para os testes
        self.controller = LightingController(luminosity_threshold=10000, presence_pin=11, cloud_enabled=False)

    def test_turn_on_lights(self):
        self.controller.turn_on_lights()
        self.assertTrue(self.controller.lights_on, "As luzes devem estar acesas.")

    def test_turn_off_lights(self):
        self.controller.turn_off_lights()
        self.assertFalse(self.controller.lights_on, "As luzes devem estar apagadas.")

if __name__ == '__main__':
    unittest.main()
