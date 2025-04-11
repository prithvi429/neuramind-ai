# Agent Manager: Handles the coordination between different agents.

from nav_agent import get_route
from image_agent import generate_image
from agents.writing_agent import generate_content
from agents.finance_agent import analyze_financial_data

def handle_request(agent_type, payload):
    """
    Handles requests by delegating them to the appropriate agent.

    Args:
        agent_type (str): The type of agent to handle the request (e.g., 'navigation', 'image', 'writing', 'finance').
        payload (dict): The input data for the agent.

    Returns:
        str: The response from the agent.
    """
    if agent_type == "navigation":
        start = payload.get("start_location")
        end = payload.get("end_location")
        return get_route(start, end)
    elif agent_type == "image":
        prompt = payload.get("prompt")
        return generate_image(prompt)
    elif agent_type == "writing":
        prompt = payload.get("prompt")
        return generate_content(prompt)
    elif agent_type == "finance":
        data = payload.get("data")
        return analyze_financial_data(data)
    else:
        return "Invalid agent type."

if __name__ == "__main__":
    # Example usage
    nav_request = {"start_location": "New York", "end_location": "Los Angeles"}
    print(handle_request("navigation", nav_request))

    image_request = {"prompt": "A futuristic cityscape at night."}
    print(handle_request("image", image_request))

    writing_request = {"prompt": "Write a short story about AI helping humanity."}
    print(handle_request("writing", writing_request))

    finance_request = {"data": {"revenue": 100000, "expenses": 75000}}
    print(handle_request("finance", finance_request))
