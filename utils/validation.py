import json


def validate_query_params(request, expected_params=None):
    """
    Validates the query parameters of a request against the expected parameters.

    :param request: The Flask request object.
    :param expected_params: A dictionary where keys are the names of expected query parameters
                            and values are the expected types (e.g., str, int).
    :return: A tuple containing a boolean indicating if validation passed,
             and a message if validation failed. Also returns a status code.
    """
    if expected_params is None or expected_params == {}:
        return True, None, 200

    for param, expected_type in expected_params.items():
        # Check if the parameter is in the request
        if param not in request.args:
            return False, f"Missing query parameter: {param}", 400

        # Validate the type of the parameter
        try:
            expected_type(request.args[param])
        except ValueError:
            return (
                False,
                f"Incorrect type for parameter: {param}. Expected {expected_type.__name__}",
                400,
            )

    return True, None, 200


def validate_request_body(request, expected_body_schema=None):
    """
    Validates the request body of a request against the expected body schema.

    :param request: The Flask request object.
    :param expected_body_schema: A dictionary where keys are the names of expected keys in the request body
                                 and values are the expected types (e.g., str, int). You can omit this parameter
                                 if you don't expect any request body.
    :return: A tuple containing a boolean indicating if validation passed,
             and a message if validation failed. Also returns a status code.
    """
    if expected_body_schema is None or expected_body_schema == {}:
        return True, None, 200

    # Check if the Content-Type header is set to application/json
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            False,
            "Unsupported Media Type: Content-Type must be application/json",
            415,
        )

    try:
        # Attempt to parse JSON from the request body
        request_body_as_text = request.get_data(as_text=True)
        request_body = json.loads(request_body_as_text)
    except json.JSONDecodeError:
        return (
            False,
            "Invalid JSON format in request body or empty",
            400,
        )

    for key, expected_type in expected_body_schema.items():
        # Check if the key is in the request body
        if key not in request_body:
            return False, f"Missing key in request body: {key}", 400

        # Validate the type of the value associated with the key
        if not isinstance(request_body[key], expected_type):
            return (
                False,
                f"Incorrect type for key: {key}. Expected {expected_type.__name__}",
                400,
            )

    return True, None, 200
