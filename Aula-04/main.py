import matplotlib.pyplot as plt
from PIL import Image

dados_telemetria_agricultura = {
    "drone_id": "CT-DRONE-06",
    "timestamp": "2026-09-11 10:51:00",
    "sensores_solo": {
        "umidade_solo": 15.2,
        "temperatura_solo": 32.2,
        "nitrogenio": 45.0
    },
    "status_plantacao": "Alerta de Estresse Critico",
    "local_imagem": "Aula-04/campo.jpg"
}

img = Image.open(dados_telemetria_agricultura["local_imagem"])

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img)
ax.axis("off")

# Define o título pegando os dados (drone_id) com tamanho

plt.title(f"Monitoramento do Campo: Drone {dados_telemetria_agricultura}")

# Prepara o bloco de texto com os dados da telemtria

info_agricultura = (
    f"TELEMETRIA DE CAMPO\n"
    f"UMIDADE DO SOLO: {dados_telemetria_agricultura['sensores_solo']}%\n"
    f"TEMPERATURA DO SOLO: {dados_telemetria_agricultura['sensores_solo']['temperatura_solo']}%\n"
    f"NIROGÊNIO: {dados_telemetria_agricultura['sensores_solo']['nitrogenio']}%\n"
    f"STATUS: {dados_telemetria_agricultura['status_plantacao']}%\n"
)

# Exibir a tela de texto com a borda e fundo customizados sobre a imagem
ax.text(0.05,0.95,info_agricultura, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='honeydew', alpha=0.9, edgecolor='darkgreen'))

plt.tight_layout()
plt.show()