import csv
import json
from collections import defaultdict

csv_path = 'Datos/mantenimiento.csv'
json_path = 'Datos/mantenimiento.json'

# Ajusta el separador según tu archivo, normalmente ; para Excel/latam
csv_delimiter = ';'

historial_por_tag = defaultdict(list)

with open(csv_path, mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=csv_delimiter)
    for row in reader:
        # Usa la columna que ahora es idéntica en ambos archivos
        tag = row['TAG MANTTO']   # Cambiado aquí
        historia = {
            'ACTIVIDAD': row.get('ACTIVIDAD', ''),
            'FECHA': row.get('FECHA', ''),
            'RESULTADO': row.get('RESULTADO', '')
        }
        historial_por_tag[tag].append(historia)

# Estructura agrupada por TAG MANTTO
json_data = [
    {'TAG MANTTO': tag, 'historial': historial}
    for tag, historial in historial_por_tag.items()
]

with open(json_path, mode='w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)

print(f'Archivo {json_path} generado correctamente.')

