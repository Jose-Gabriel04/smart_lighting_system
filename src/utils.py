import json
import os

def load_json_file(file_path):
    """Carrega dados de um arquivo JSON"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON no arquivo {file_path}.")
        return {}

def save_json_file(file_path, data):
    """Salva dados em um arquivo JSON"""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar arquivo JSON {file_path}: {e}")

def check_gpio_pin(pin):
    """Verifica se o pino GPIO informado é válido"""
    if not isinstance(pin, int) or not (0 <= pin <= 40):
        raise ValueError(f"O pino GPIO {pin} é inválido. Escolha um número entre 0 e 40.")

def handle_exception(func):
    """Decora funções para capturar exceções e registrar logs"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erro encontrado: {e}")
            return None
    return wrapper