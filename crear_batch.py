# crear_batch.py

ruta_carpeta = r"C:\Users\Martha Rubiano\Downloads\demo gas 2"
nombre_archivo = "iniciar_visor.bat"

contenido = f"""@echo off
cd /d "{ruta_carpeta}"
start "" http://localhost:8001/visor.html
python -m http.server 8001
pause
"""

# Guardar el archivo .bat
with open(f"{ruta_carpeta}\\{nombre_archivo}", "w") as archivo:
    archivo.write(contenido)

print(f"✅ Archivo {nombre_archivo} creado exitosamente en {ruta_carpeta}")
