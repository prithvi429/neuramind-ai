from backend.nav_agent import get_route

def main():
    """
    Runs the navigation agent with example inputs.
    """
    start_location = "New York"
    end_location = "Los Angeles"
    route = get_route(start_location, end_location)
    print(route)

if __name__ == "__main__":
    main()
