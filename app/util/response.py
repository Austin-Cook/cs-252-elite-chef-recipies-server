from flask import jsonify, Response
from typing import Tuple

from app.settings import MESSAGE, RETRIEVED_FROM

# SUCCESS

def res_ok_add() -> Tuple[Response, int]:
    return _json_success("Recipe saved to MongoDB"), 200

def res_ok_delete(num_deleted: int) -> Tuple[Response, int]:
    return _json_success("Deleted " + str(num_deleted) + " recipies from MongoDB Atlas"), 200

def resp_ok_find(recipe: dict, retrieved_from: str):
    recipe[MESSAGE] = "Success: Found a matching recipe in " + retrieved_from
    recipe[RETRIEVED_FROM] = retrieved_from
    return jsonify(recipe), 200

# ERROR

def res_err_field_empty(field: str) -> Tuple[Response, int]:
    return _json_error("Empty field in request: " + field), 400

def res_err_field_missing(field: str) -> Tuple[Response, int]:
    return _json_error("Missing field in request: " + field), 400

def res_err_field_too_large(field: str, maxSize: int, actualSize: int) -> Tuple[Response, int]:
    return _json_error("Field too large: " + field + " " + str(actualSize) + "/" + str(maxSize) + " characters"), 400

def res_err_missing_query_param(param: str):
    return _json_error("Request missing query param: " + param), 400

def res_err_no_matching_item(item: str) -> Tuple[Response, int]:
    return _json_error("No matching item in Redis cache or MongoDB: " + item), 404

def res_err_not_json() -> Tuple[Response, int]:
    return _json_error("Request content was not JSON"), 400

def res_err_unable_to_add_to_mongo() -> Tuple[Response, int]:
    return _json_error("Internal server error: Unable to add recipe to MongoDB Atlas"), 500

def res_err_wrong_type(field: str) -> Tuple[Response, int]:
    return _json_error("Input parameter should be of type string: " + field), 400

# HELPER METHODS

def _json_error(message: str) -> Response:
    return jsonify({
        MESSAGE: "Error: " + message
    })
    
def _json_success(message: str) -> Response:
    return jsonify({
        MESSAGE: "Success: " + message
    })
