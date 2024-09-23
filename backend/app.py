from flask import Flask, jsonify
from vaga_proxima import encontrar_vaga_mais_proxima

app = Flask(__name__)

@app.route('/proxima_vaga', methods=['GET'])
def proxima_vaga():
    vaga_proxima = encontrar_vaga_mais_proxima()
    return jsonify(vaga_proxima)

if __name__ == '__main__':
    app.run(debug=True)
