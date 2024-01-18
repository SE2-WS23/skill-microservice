from prisma import Prisma
from flask import request, jsonify
from utils.validation import validate_request_body

prisma = Prisma()
prisma.connect()

def put(request, skill_id):
    """
    Update an existing skill in the database.

    :param request: The `request` parameter is the HTTP request object that contains information about
    the incoming request, such as the request method, headers, and body.
    :param skill_id: The ID of the skill to be updated.
    :return: The response data and headers, along with a status code.
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

        updated_skill = prisma.skill.update({
            'where': {'id': skill_id},
            'data': {
                'skillName': data.get('skillName', None),
                'description': data.get('description', None),
                'category': data.get('category', None),
                'level': data.get('level', None)
            }
        })

        if updated_skill:
            updated_skill_data = {
                'id': updated_skill.id,
                'skillName': updated_skill.skillName,
                'description': updated_skill.description,
                'category': updated_skill.category,
                'level': updated_skill.level
            }

            response['data'] = updated_skill_data
            return jsonify(response), 200, header
        else:
            response['message'] = 'Skill not found'
            return jsonify(response), 404, header

    except Exception as e:
        response['message'] = str(e)
        return jsonify(response), 500, header