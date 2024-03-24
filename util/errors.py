from flask import jsonify

def get_json_error(message:str):
    return jsonify({
        "message": "Error: " + str
    })

def error_not_json():
    return get_json_error("Request content was not JSON")

def error_field_missing(field: str):
    return get_json_error("Missing field in request: " + field)

def error_field_empty(field: str):
    return get_json_error("Empty field in request: " + field)

def error_field_too_large(field: str, maxSize: int, actualSize: int):
    return get_json_error("Field too large: " + field + " " + actualSize + "/" + actualSize + " characters")

def error_wrong_type(field: str):
    return get_json_error("Input parameter should be of type string: " + field)

def error_item_not_in_db(item: str):
    return get_json_error("Not found in Redis cache or MongoDB: " + item)
