import time
import Adafruit_ADS1x15

class LuminositySensor:
    def __init__(self):
        # Usa o ADC ADS1115 para ler os valores do sensor de luminosidade (LDR)
        self.adc = Adafruit_ADS1x15.ADS1115()

    def read_value(self):
        try:
            # Lê o valor analógico da entrada do sensor (0-32767)
            luminosity = self.adc.read_adc(0, gain=1)
            return luminosity
        except Exception as e:
            print(f"Erro na leitura do sensor de luminosidade: {e}")
            return 0