def format_response(data):
    """
    Formats the response data into a standard structure.

    Args:
        data (dict): The data to format.

    Returns:
        dict: The formatted response.
    """
    return {"status": "success", "data": data}
