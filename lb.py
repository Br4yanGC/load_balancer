from flask import Flask
import requests 

app = Flask(__name__)

# Lista de servidores backend con pesos
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

    backend_servers.sort(key=lambda x: x["weight"], reverse=True)
    
    # Obtener el servidor correspondiente al índice actual
    current_server = backend_servers[request_counter % total_servers]
    
    # Verificar la capacidad del servidor
    if current_server["capacity"] > 0:
        current_server["capacity"] -= 1
        response = requests.get(current_server["url"])
        return response.content, response.status_code
    else:
        # Si el servidor está a capacidad, intentar con el siguiente servidor
        request_counter += 1
        return load_balancer()

if __name__ == '__main__':
    # Cambia el valor de 'port' al puerto que desees utilizar
    app.run(debug=True, port=5005)  
