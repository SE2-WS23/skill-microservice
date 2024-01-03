from utils.validation import validate_request_body


def post(request, response, header, *args, **kwargs):
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
    # Validate query parameters
    expected_params = {
        "param1": str,
        "param2": int,
    }  # Define your expected parameters and their types
    validation_passed, error_message, status_code = validate_request_body(
        request, expected_params
    )

    if not validation_passed:
        response = {"message": error_message}
        return response, status_code, header

    # Change Data
    response["data"] = "Hello World!"
    header["example"] = "example"

    return response, 200, header
