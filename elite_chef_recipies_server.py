from flask import Flask, request
from util.query_handler import QueryHandler
from util.util import *

app = Flask(__name__)
handler = QueryHandler()

@app.route('/recipe', methods=['GET'])
def get_recpie():
    return handler.process_get(request)

@app.route('/recipe', methods=['POST'])
def post_recipe():
    return handler.process_post()

@app.route('/recipe', methods=['DELETE'])
def delete_all_for_user():
    return handler.process_delete()


if __name__ == "__main__":
    app.run(debug=True)
