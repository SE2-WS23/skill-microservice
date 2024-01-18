from utils.validation import validate_query_params
from prisma import Prisma 

prisma = Prisma()
prisma.connect()

def get_skills(request, response, header):
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

    # Extract query parameter 'only' if present
    only = request.args.get("only")
    if only:
        skills = prisma.skill.find_many(
            where={'tags': {'has_some': only.split(',')}})
    else:
        skills = prisma.skill.find_many()

    response["data"] = [skill.__dict__ for skill in skills]
    header["Content-Type"] = "application/json"

    return response, 200, header

def get_skill_by_id(request, response, header, skill_id):
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

    skill = prisma.skill.find_unique(where={'id': int(skill_id)})
    if skill:
        response["data"] = skill.__dict__
        header["Content-Type"] = "application/json"
        return response, 200, header
    else:
        response['message'] = 'Skill not found'
        return response, 404, header