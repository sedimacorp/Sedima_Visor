import csv
import json
import os

# Ruta a la carpeta "Datos"
carpeta = os.path.join("Datos")

# Ruta completa de entrada y salida
archivo_csv = os.path.join(carpeta, 'PlanMantenimiento.csv')
archivo_json = os.path.join(carpeta, 'PlanMantenimiento.json')

# Leer el CSV y convertirlo en una lista de diccionarios
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Escribir en formato JSON
with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4, ensure_ascii=False)

print(f'✅ Archivo JSON creado: {archivo_json}')
