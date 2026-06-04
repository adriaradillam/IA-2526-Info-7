import matplotlib.pyplot as plt
import numpy as np

# 1. Gráfico de AP por consulta
queries = [f'Q{i}' for i in range(1, 36)]
aps = [
    0.2333, 0.2659, 0.0707, 0.6383, 0.3859, 0.5769, 1.0000, 0.0455, 1.0000, 0.4167,
    0.5195, 0.0323, 0.2922, 1.0000, 0.3611, 1.0000, 0.2917, 0.1238, 0.7000, 0.5556,
    0.5000, 0.0455, 0.1429, 0.5278, 0.1111, 0.3333, 0.0000, 0.0000, 0.0250, 1.0000,
    0.3333, 0.0135, 0.1429, 0.2698, 0.0213
]

plt.figure(figsize=(14, 5))
plt.bar(queries, aps, color='steelblue')
plt.axhline(y=np.mean(aps), color='r', linestyle='--', label=f'MAP: {np.mean(aps):.4f}')
plt.title('Average Precision (AP) por Necesidad de Información', fontsize=14)
plt.xlabel('Consulta', fontsize=12)
plt.ylabel('AP', fontsize=12)
plt.ylim(0, 1.1)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('ap_chart.png', dpi=300)

# 2. Gráfico de métricas globales Vectorial
metrics = ['Precisión', 'Sensibilidad (Recall)', 'MAP']
values = [0.0176, 0.9429, 0.3707]
colors = ['lightcoral', 'mediumseagreen', 'steelblue']

plt.figure(figsize=(8, 5))
bars = plt.bar(metrics, values, color=colors)
plt.title('Métricas Globales - Modelo Vectorial (TF-IDF)', fontsize=14)
plt.ylabel('Valor', fontsize=12)
plt.ylim(0, 1.15)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f'{yval*100:.2f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('metrics_chart.png', dpi=300)

print('Graficas generadas con exito.')
