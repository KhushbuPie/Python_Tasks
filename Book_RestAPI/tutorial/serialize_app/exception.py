from rest_framework.exceptions import APIException

class CustoAPIException(APIException):
    status_code = 500
    default_detail = 'A server error occurred.'
    default_code = 'server_error'