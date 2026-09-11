import matplotlib.pyplot as plt
from PIL import Image

dados_telemetria_fliperama = {
    "fliperama_id": "fliperama_gaymer",
    "timestamp": "2026-09-11 11:33:00",
    "sensor_desempenho": {
        "FPS": 60,
        "TEMPERATURA_GPU": 70,
        "LATÊNCIA": 12.2
    }, 
    "status_fliperama": "Moderado",
    "local_image": "Aula-04/fliperama.jpg"
}

img = Image.open(dados_telemetria_fliperama["local_image"])

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img)
ax.axis("off")

# Define o título pegando os dados do fliperama

plt.title(f"Monitoramento do fliperama: {dados_telemetria_fliperama}")

# prepara o bloco de texto

info_fliperama = (
    f"TELEMETRIA FLIPERAMA\n"
    f"FPS: {dados_telemetria_fliperama['sensor_desempenho']['FPS']}\n"
    f"TEMPERATURA DA GPU: {dados_telemetria_fliperama['sensor_desempenho']['TEMPERATURA_GPU']}\n"
    f"LATÊNCIA: {dados_telemetria_fliperama['sensor_desempenho']['LATÊNCIA']}\n"
    f"STATUS DO FLIPERAMA: {dados_telemetria_fliperama['status_fliperama']}"
)

# Exibir a tela de texto com a borda e fundo customizados sobre a imagem
ax.text(0.05,0.95, info_fliperama, transform=ax.transAxes, fontsize=11,

        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='honeydew', alpha=0.9, edgecolor='darkgreen'))
plt.tight_layout()
plt.show()