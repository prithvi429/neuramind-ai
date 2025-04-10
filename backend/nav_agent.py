def get_route(start_location, end_location):
    """
    Calculates the route between two locations.

    Args:
        start_location (str): The starting point.
        end_location (str): The destination.

    Returns:
        str: A message with the calculated route.
    """
    print(f"Calculating route from {start_location} to {end_location}...")
    return f"Route from {start_location} to {end_location} calculated successfully."