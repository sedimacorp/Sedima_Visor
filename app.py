from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'Datos/mantenimiento.csv'

@app.route('/agregar_mantto', methods=['POST'])
def agregar_mantto():
    data = request.json
    # Verifica que existan todos los campos requeridos
    for campo in ['TAG MANTTO', 'ACTIVIDAD', 'FECHA', 'RESULTADO']:
        if campo not in data:
            return jsonify({'status': 'error', 'msg': f'Falta el campo {campo}'}), 400

    existe = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        if not existe:
            writer.writerow(['TAG MANTTO', 'ACTIVIDAD', 'FECHA', 'RESULTADO'])
        writer.writerow([
            data['TAG MANTTO'],
            data['ACTIVIDAD'],
            data['FECHA'],
            data['RESULTADO']
        ])

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # debug=True solo para desarrollo/test
    app.run(debug=True)
