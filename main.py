from utils.preflight import handle_preflight
import functions_framework
from methods.get import get_skills, get_skill_by_id
from methods.post import post

NEED_CORS_PREFLIGHT_RESPONSE = True
ALLOWED_ORIGINS = "*"
SUPPORTED_METHODS = ["GET", "POST", "OPTIONS"]


@functions_framework.http
def http_function(request):
    """
    The above function is a template for an HTTP function that handles different HTTP methods and
    returns a response, status code, and header based on the request method.

    :param request: The `request` parameter is an object that represents the HTTP request made to the
    server. It contains information such as the HTTP method (GET, POST, etc.), headers, query
    parameters, and the request body. It is derived from the Flask request object.
    :return: three values: `response`, `status_code`, and `header`.
    """
    header = {}
    response = {}
    status_code = 200

    # Don't change this
    if request.method not in SUPPORTED_METHODS:
        return "", 405, header

    # Don't change this
    if NEED_CORS_PREFLIGHT_RESPONSE:
        header["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
        if request.method == "OPTIONS":
            # Handle CORS preflight request
            return handle_preflight(allowed_methods=SUPPORTED_METHODS)

    # ToDo: Link your methods from methods/ here
    # ToDo: Set header, status_code and response. You response can have any value
    # that can be turned into a Repsonse object using `make_reponse'.
    # See more https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
    try:
        if request.method == "GET":
            # Check for a specific skill ID in the path
            skill_id = request.args.get('id')
            if skill_id:
                response, status_code, header = get_skill_by_id(request, response, header, skill_id)
            else:
                response, status_code, header = get_skills(request, response, header)

        elif request.method == "POST":
            response, status_code, header = post(request, response, header)

        else:
            response = {"message": "Method not supported"}
            status_code = 405

    except Exception as e:
        response = {"message": str(e)}
        status_code = 500
    
    return response, status_code, header


# For testing purposes only!
# It is easier to develop your function without the need to restart your cloud function every time
# But keep in mind that this is not completely the same environment as in the cloud function environment
if __name__ == "__main__":
    # ToDo: Add your function here

    pass
