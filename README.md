# smart_lighting_system

# Sistema de Iluminação Inteligente com IoT

## Visão Geral

Este sistema de iluminação inteligente utiliza sensores IoT para monitorar a luminosidade e a presença em ambientes, controlando automaticamente as luzes com o objetivo de reduzir o consumo de energia elétrica. Além disso, simula a integração com serviços em nuvem para armazenar dados.

### Funcionalidades
- Monitoramento contínuo da luminosidade e da presença.
- Controle automático da iluminação com base nas leituras dos sensores.
- Registro detalhado de logs de eventos e erros.
- Integração simulada com a nuvem para armazenamento de dados.
- Interface de linha de comando (CLI) para controle do sistema.

## Estrutura do Projeto

- `src/`: Arquivos principais do sistema.
  - `sensors/`: Módulos que simulam os sensores de presença e luminosidade.
  - `controllers/`: Controlador responsável pela lógica do sistema de iluminação.
  - `services/`: Serviço simulado de integração com a nuvem.
  - `cli/`: Interface de linha de comando para controle do sistema.
  - `logger.py`: Função para registro de logs.
  - `main.py`: Inicia o sistema.
- `config/`: Configurações do sistema.
- `data/`: Registros de eventos e logs de erros.
- `tests/`: Testes automatizados.

## Como Executar

1. Clone o repositório, instale as dependências, configure os parâmetros em settings.json e execute o sistema:

```bash
git clone https://github.com/seuusuario/smart_lighting_system.git
pip install -r requirements.txt
python src/main.py