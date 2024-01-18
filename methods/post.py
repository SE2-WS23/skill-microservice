from utils.validation import validate_request_body
from prisma import Prisma
from flask import request, jsonify

prisma = Prisma()
prisma.connect()

def post(request):
    """
    The function modifies the response data and header, and returns them along with a status code.

    :param request: The `request` parameter is the HTTP request object that contains information about
    the incoming request, such as the request method, headers, and body. It is used to retrieve
    information from the request
    :param response: The `response` parameter is a dictionary that represents the response data that
    will be sent back to the client.
    :param header: The `header` parameter is a dictionary that contains the HTTP headers for the
    response. It is used to set custom headers for the response
    :return: the updated response, the HTTP status code, and the updated header.
    """
    response = {}
    header = {'Content-Type': 'application/json'}

    expected_body_schema = {
        'skillName': str,
        'description': str,
        'category': str,
        'level': str
    }

    validation_passed, error_message, status_code = validate_request_body(request, expected_body_schema)

    if not validation_passed:
        response['message'] = error_message
        return jsonify(response), status_code, header

    try:
        data = request.json

        new_skill = prisma.skill.create(data={
            'skillName': data['skillName'],
            'description': data['description'],
            'category': data['category'],
            'level': data['level']
        })
        new_skill_data = {
            'id': new_skill.id,
            'skillName': new_skill.skillName,
            'description': new_skill.description,
            'category': new_skill.category,
            'level': new_skill.level
        }

        response['data'] = new_skill_data
        return jsonify(response), 201, header

    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500, header