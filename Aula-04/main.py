import matplotlib as plt
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
    "local_imagem": "campo.jpg"
}

img = Image.open(dados_telemetria_agricultura["local_imagem"])

fig, ax = plt.subplots(figsize=(10, 6))
ax.imShow(img)
ax.axis("off")

plt.title(f"Monitoramento do Campo: Drone {dados_telemetria_agricultura}")