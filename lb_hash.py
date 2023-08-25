from flask import Flask, request
import requests 

app = Flask(__name__)

# Lista de servidores backend con pesos y capacidad
backend_servers = [
    {"url": "http://127.0.0.1:5002/hello", "weight": 2, "capacity": 3},
    {"url": "http://127.0.0.1:5001/hello", "weight": 5, "capacity": 3},
    {"url": "http://127.0.0.1:5003/hello", "weight": 1, "capacity": 3},
]

total_servers = len(backend_servers)
request_counter = 0

@app.route('/')
def load_balancer():
    global request_counter
    
    # Obtener la URL del servidor correspondiente a la hash de la URL de la solicitud
    hash_value = hash(request_counter)
    current_server = backend_servers[hash_value % total_servers]
    request_counter += 1
    

    response = requests.get(current_server["url"])
    return response.content, response.status_code

if __name__ == '__main__':
    # Cambia el valor de 'port' al puerto que desees utilizar
    app.run(debug=True, port=5005)
