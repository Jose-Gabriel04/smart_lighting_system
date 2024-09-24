from sensors.presence_sensor import PresenceSensor
from sensors.luminosity_sensor import LuminositySensor
from services.cloud_service import CloudService
from logger import log_event
import time

class LightingController:
    def __init__(self, luminosity_threshold, presence_pin, cloud_enabled=False):
        self.luminosity_sensor = LuminositySensor()
        self.presence_sensor = PresenceSensor(presence_pin)
        self.luminosity_threshold = luminosity_threshold
        self.lights_on = False
        self.cloud_service = CloudService() if cloud_enabled else None

    def manage_lights(self):
        try:
            while True:
                luminosity = self.luminosity_sensor.read_value()
                presence = self.presence_sensor.read_value()

                if luminosity < self.luminosity_threshold and presence:
                    self.turn_on_lights()
                else:
                    self.turn_off_lights()

                if self.cloud_service:
                    self.cloud_service.upload_data({"luminosity": luminosity, "presence": presence, "lights_on": self.lights_on})

                log_event(f"Luminosity: {luminosity}, Presence: {presence}, Lights On: {self.lights_on}")
                time.sleep(5)
        except Exception as e:
            self.handle_error(e)

    def turn_on_lights(self):
        if not self.lights_on:
            print("Luzes acesas.")
            self.lights_on = True
            log_event("Luzes acesas")

    def turn_off_lights(self):
        if self.lights_on:
            print("Luzes apagadas.")
            self.lights_on = False
            log_event("Luzes apagadas")

    def handle_error(self, error):
        with open('../data/error_log.txt', 'a') as error_file:
            error_file.write(f"Erro: {str(error)}\n")
        log_event(f"Erro capturado: {error}")
        print(f"Erro capturado: {error}")