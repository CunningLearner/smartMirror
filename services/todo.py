from flask import Flask, jsonify, make_response
import json
import os

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open('{}/database/todo.json'.format(database_path), "r") as jsf:
    todo_list = json.load(jsf)

@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Todo service is up"

if __name__ == '__main__':
    app.run(port=5018, debug=True)
