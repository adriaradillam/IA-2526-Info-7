import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys

# Cambiamos al directorio del proyecto para que las rutas relativas funcionen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Leer necesidades
necesidades = []
with open('../necesidades_info/necesidades.csv', 'r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        docs_rel = [n.strip() + '.txt' for n in fila['relevantes'].strip().split(',') if n.strip()]
        necesidades.append({
            'id': int(fila['id']),
            'consulta_booleana': fila['consulta_booleana'].strip(),
            'relevantes': docs_rel
        })

# Simular la busqueda booleana con Whoosh para sacar los numeros reales
from whoosh import index
from whoosh.qparser import QueryParser, AndGroup

DIRECTORIO_INDICE = "../indice_booleano"
ix = index.open_dir(DIRECTORIO_INDICE)

precisions = []
recalls = []

for n in necesidades:
    parser = QueryParser('contenido', schema=ix.schema, group=AndGroup)
    consulta = parser.parse(n['consulta_booleana'])

    with ix.searcher() as searcher:
        resultados = searcher.search(consulta, limit=None)
        recuperados = set([hit['titulo'] for hit in resultados])

    relevantes = set(n['relevantes'])
    tp = recuperados & relevantes

    prec = len(tp) / len(recuperados) if recuperados else 0.0
    rec = len(tp) / len(relevantes) if relevantes else 0.0

    precisions.append(prec)
    recalls.append(rec)

    print(f"Q{n['id']:>2}: Recup={len(recuperados):>3}, Relev={len(relevantes)}, TP={len(tp)}, Prec={prec:.4f}, Recall={rec:.4f}")

print(f"\nPrecision media: {np.mean(precisions):.4f} ({np.mean(precisions)*100:.2f}%)")
print(f"Recall medio:    {np.mean(recalls):.4f} ({np.mean(recalls)*100:.2f}%)")

# 1. Grafico de Precision por consulta (modelo booleano)
queries = [f'Q{i}' for i in range(1, 21)]

plt.figure(figsize=(10, 5))
plt.bar(queries, precisions, color='darkorange', label='Precisión')
plt.axhline(y=np.mean(precisions), color='r', linestyle='--',
            label=f'Media: {np.mean(precisions)*100:.2f}%')
plt.title('Precisión por Necesidad de Información - Modelo Booleano', fontsize=14)
plt.xlabel('Consulta', fontsize=12)
plt.ylabel('Precisión', fontsize=12)
plt.ylim(0, 1.1)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('bool_precision_chart.png', dpi=300)
print("Guardado: bool_precision_chart.png")

# 2. Grafico comparativo Booleano vs Vectorial
metrics = ['Precisión', 'Sensibilidad (Recall)']
bool_vals = [np.mean(precisions), np.mean(recalls)]
vec_vals = [0.0700, 1.0000]

x = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(8, 5))
bars1 = plt.bar(x - width/2, bool_vals, width, label='Modelo Booleano', color='darkorange')
bars2 = plt.bar(x + width/2, vec_vals, width, label='Modelo Vectorial', color='steelblue')

plt.title('Comparativa de Métricas - Booleano vs Vectorial', fontsize=14)
plt.ylabel('Valor', fontsize=12)
plt.ylim(0, 1.25)
plt.xticks(x, metrics, fontsize=11)
plt.legend()

for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02,
             f'{yval*100:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02,
             f'{yval*100:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('bool_vs_vec_chart.png', dpi=300)
print("Guardado: bool_vs_vec_chart.png")
