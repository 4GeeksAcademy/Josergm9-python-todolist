from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

todos = [
   { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify (todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Esta es la posicion que se elimino:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "indice fuera de rango", "todos": todos}), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)