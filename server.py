from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import persistencia


app = Flask("multivix")
CORS(app)

@app.route('/api/tarefas', methods=['GET'])
def obter():
    tarefas = persistencia.carregar()
    return jsonify(tarefas)

@app.route('/api/tarefas', methods=['POST'])
def incluir():
    tarefa = request.get_json()
    print("estou aqui")
    persistencia.salvar(tarefa)
    resultado = { "mensagem": 'Registro salvo' }
    return jsonify({'result': resultado})


# Para subir o servidor use:
# flask --app server run

#iniciar aplicacao
if __name__ == '__main__':
	app.run(debug=True)
