def handle_preflight(
    allowed_methods=["POST", "GET", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allowed_headers=["Content-Type"],
    max_age="3600",
):
    """
    The `handle_preflight` function sets the necessary headers for handling preflight requests in a web
    application.

    :param allowed_methods: A list of HTTP methods that are allowed for the preflight request. The
    default value includes common methods such as POST, GET, PUT, PATCH, DELETE, and OPTIONS
    :param allowed_headers: The `allowed_headers` parameter is a list of headers that are allowed in the
    preflight request. In this case, only the "Content-Type" header is allowed
    :param max_age: The `max_age` parameter specifies the maximum time in seconds that the preflight
    response can be cached by the client. In this case, it is set to "3600", which means the preflight
    response can be cached for 1 hour, defaults to 3600 (optional)
    :return: an empty string, a status code of 204 (No Content), and a dictionary of headers.
    """
    headers = {
        "Access-Control-Allow-Methods": ", ".join(allowed_methods),
        "Access-Control-Allow-Headers": ", ".join(allowed_headers),
        "Access-Control-Max-Age": max_age,
    }

    return "", 204, headers
