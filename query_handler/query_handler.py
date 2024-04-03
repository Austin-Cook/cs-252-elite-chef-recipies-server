from flask import Request
from data_access.db_manager import DBManager
from util.util import strip_whitespace, char_count
from util.response import response_error_not_json, response_error_field_missing, response_error_field_empty, response_error_field_too_large, response_error_wrong_type, response_error_missing_query_param
from util.util import get_logger
from settings import QUERY_MAX_LEN, EMAIL_MAX_LEN, TITLE_MAX_LEN, TAG_MAX_LEN, DESCRIPTION_MAX_LEN, QUERY, EMAIL, TITLE, TAG1, TAG2, TAG3, DESCRIPTION
import json


class QueryHandler:
    def __init__(self, db_manager: DBManager):
        self.logger = get_logger(self.__class__.__name__)
        self.db_manager = db_manager

    def process_get(self, request: Request):
        query = request.args.get(QUERY)
        if (query is None):
            return response_error_missing_query_param(QUERY)        
        query = strip_whitespace(query)
        len = char_count(query)
        if (len == 0):
            return response_error_field_empty(QUERY)
        if (len > QUERY_MAX_LEN):
            return response_error_field_too_large(QUERY, QUERY_MAX_LEN, len)  

        return self.db_manager.get(query)
        

    def process_post(self, request: Request):
        self.logger.debug("POST request: " + json.dumps(request.json))
        if not request.is_json:
            return response_error_not_json()
        json_data = request.json
        if not EMAIL in json_data:
            return response_error_field_missing(EMAIL)
        if not TITLE in json_data:
            return response_error_field_missing(TITLE)
        if not DESCRIPTION in json_data:
            return response_error_field_missing(DESCRIPTION)
        if not isinstance(json_data[EMAIL], str):
            return response_error_wrong_type(EMAIL)
        if not isinstance(json_data[TITLE], str):
            return response_error_wrong_type(TITLE)
        if not isinstance(json_data[DESCRIPTION], str):
            return response_error_wrong_type(DESCRIPTION)
        email = strip_whitespace(json_data[EMAIL])
        title = strip_whitespace(json_data[TITLE])
        description = strip_whitespace(json_data[DESCRIPTION])
        email_len = char_count(email)
        title_len = char_count(title)
        description_len = char_count(description)
        if (email_len == 0):
            return response_error_field_empty(EMAIL)
        if (title_len == 0):
            return response_error_field_empty(TITLE)
        if (description_len == 0):
            return response_error_field_empty(DESCRIPTION)
        if (email_len > EMAIL_MAX_LEN):
            return response_error_field_too_large(EMAIL, EMAIL_MAX_LEN, email_len)
        if (title_len > TITLE_MAX_LEN):
            return response_error_field_too_large(TITLE, TITLE_MAX_LEN, title_len)
        if (description_len > DESCRIPTION_MAX_LEN):
            return response_error_field_too_large(DESCRIPTION, DESCRIPTION_MAX_LEN, description_len)
        # tags of len 0 are not used
        tag1 = None
        tag2 = None
        tag3 = None
        tag = json_data.get(TAG1)
        if tag is not None:
            if not isinstance(tag, str):
                return response_error_wrong_type(TAG1)
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return response_error_field_too_large(TAG1, TAG_MAX_LEN, len)
            if len > 0:
                tag1 = tag
        tag = json_data.get(TAG2)
        if tag is not None:
            if not isinstance(tag, str):
                return response_error_wrong_type(TAG2)
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return response_error_field_too_large(TAG2, TAG_MAX_LEN, len)
            if len > 0:
                tag2 = tag
        tag = json_data.get(TAG3)
        if tag is not None:
            if not isinstance(tag, str):
                return response_error_wrong_type(TAG3)
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return response_error_field_too_large(TAG3, TAG_MAX_LEN, len)
            if len > 0:
                tag3 = tag
        
        return self.db_manager.post(email=email, title=title, description=description, 
                                    tag1=tag1, tag2=tag2, tag3=tag3)

    def process_delete(self, request: Request):
        email = request.args.get(EMAIL)
        if (email is None):
            return response_error_missing_query_param(EMAIL)
        email = strip_whitespace(email)
        len = char_count(email)
        if (len == 0):
            return response_error_field_empty(EMAIL)
        if (len > EMAIL_MAX_LEN):
            return response_error_field_too_large(EMAIL, EMAIL_MAX_LEN, len)
        
        return self.db_manager.delete(email)
