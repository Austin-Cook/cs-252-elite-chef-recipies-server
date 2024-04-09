from flask import Flask, request
from flask_cors import CORS
from app.query_handler import QueryHandler

app = Flask(__name__)
CORS(app)
handler = QueryHandler()


@app.route('/recipe', methods=['GET'])
def get_recpie():
    return handler.process_get(request)

@app.route('/recipe', methods=['POST'])
def post_recipe():
    return handler.process_post(request)

@app.route('/recipe', methods=['DELETE'])
def delete_all_for_user():
    return handler.process_delete(request)


if __name__ == "__main__":
    app.run(debug=True)
