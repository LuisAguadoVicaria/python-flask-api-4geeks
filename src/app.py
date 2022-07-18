from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": True },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)
    return jsonify(todos)
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[int(position)-1]
    print("This is the position to delete: ",position)
    return {'action': 'deleted: '+str(position), "res": todos}

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

"""
  #los test están rotos

fetch('https://3245-breathecode-pythonflask-nns56bnjalf.ws-eu47.gitpod.io/todos/1', {
  method: 'DELETE', headers: {
    'Content-Type': 'application/json'
  }, body: null})
.then(res => res.json()).then(res => console.log(res))

fetch('https://3245-breathecode-pythonflask-nns56bnjalf.ws-eu47.gitpod.io/todos', {
  method: 'POST', headers: {
    'Content-Type': 'application/json'
  }, body: JSON.stringify({ "done": true, "label": "Sample Todo 1" }) })
.then(res => res.json()).then(res => console.log(res))

"""