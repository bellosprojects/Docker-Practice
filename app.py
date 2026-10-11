import os
import socket
from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Configuracion mediante variables de entorno del sistema
REDIS_HOST = os.getenv('REDIS_HOST', 'nodo_db')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# Conexion con el almacen a traves del DNS interno
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route('/')
def index():
    try:
        visitas = db.incr('contador_visitas')
        return jsonify({
            "mensaje": "Sistemas Operativos UCV - Contenerizacion Exitosa",
            "hostname_contenedor": socket.gethostname(),
            "total_visitas": visitas,
            "estado_db": "Conectado"
        }), 200
    except redis.exceptions.ConnectionError as err:
        return jsonify({
            "error": "Fallo de conexion con el servicio de persistencia",
            "detalle": str(err)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
