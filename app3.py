from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    response = {'message': 'Success3'}
    return jsonify(response)

if __name__ == '__main__':
    # Cambia el valor de 'port' al puerto que desees utilizar
    app.run(debug=True, port=5003)  # Por ejemplo, aquí se usa el puerto 5001