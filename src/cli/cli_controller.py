from controllers.lighting_controller import LightingController
import json

def load_settings():
    with open('../config/settings.json', 'r') as file:
        settings = json.load(file)
    return settings

def start_cli():
    print("Bem-vindo ao Sistema de Iluminação Inteligente")
    while True:
        print("\nMenu:")
        print("1. Iniciar Sistema de Iluminação")
        print("2. Configurar Limite de Luminosidade")
        print("3. Configurar Pino do Sensor de Presença")
        print("4. Ativar/Desativar Integração com Nuvem")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            settings = load_settings()
            controller = LightingController(
                settings['luminosity_threshold'], 
                settings['presence_pin'], 
                cloud_enabled=settings['cloud_enabled']
            )
            controller.manage_lights()
        elif choice == "2":
            new_threshold = float(input("Defina o novo limite de luminosidade: "))
            settings = load_settings()
            settings['luminosity_threshold'] = new_threshold
            with open('../config/settings.json', 'w') as file:
                json.dump(settings, file)
            print("Limite de luminosidade atualizado.")
        elif choice == "3":
            new_pin = int(input("Defina o pino GPIO do sensor de presença: "))
            settings = load_settings()
            settings['presence_pin'] = new_pin
            with open('../config/settings.json', 'w') as file:
                json.dump(settings, file)
            print("Pino do sensor de presença atualizado.")
        elif choice == "4":
            settings = load_settings()
            settings['cloud_enabled'] = not settings['cloud_enabled']
            with open('../config/settings.json', 'w') as file:
                json.dump(settings, file)
            print(f"Integração com nuvem {'ativada' if settings['cloud_enabled'] else 'desativada'}.")
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")