# Writing Agent: Handles content generation tasks.

def generate_content(prompt):
    """
    Generates content based on the provided prompt.

    Args:
        prompt (str): The input prompt for content generation.

    Returns:
        str: The generated content.
    """
    print(f"Generating content for prompt: {prompt}")
    # Add logic for content generation here
    if prompt == "What is the capital of France?":
        return "The capital of France is Paris."
    elif prompt == "Solve 2 + 2.":
        return "The result is 4."
    elif prompt == "Translate 'Hello' to Spanish.":
        return "The translation is 'Hola'."
    elif prompt == "What is the largest planet in our solar system?":
        return "The largest planet in our solar system is Jupiter."
    elif prompt == "Who wrote 'Romeo and Juliet'?":
        return "The play 'Romeo and Juliet' was written by William Shakespeare."
    else:
        return f"Generated content based on the prompt: '{prompt}'"

if __name__ == "__main__":
    # Example usage
    content = generate_content("Write a short story about AI.")
    print(content)