import openai

# Image Agent: Handles image generation and editing tasks.

class ImageAgent:
    def __init__(self):
        """
        Initializes the ImageAgent with OpenAI API key.
        """
        openai.api_key = "YOUR_API_KEY"

    def generate_image(self, prompt):
        """
        Generates an image based on the provided prompt.

        Args:
            prompt (str): The description of the image to generate.

        Returns:
            str: The URL of the generated image.
        """
        response = openai.Image.create(prompt=prompt, n=1, size="512x512")
        return response['data'][0]['url']

def edit_image(image_path, instructions):
    """
    Edits an image based on the provided instructions.

    Args:
        image_path (str): The path to the image to be edited.
        instructions (str): The editing instructions.

    Returns:
        str: A message indicating the editing status.
    """
    print(f"Editing image at {image_path} with instructions: {instructions}")
    # Add logic for image editing here
    return f"Image at '{image_path}' edited successfully with instructions: '{instructions}'"

if __name__ == "__main__":
    # Example usage
    agent = ImageAgent()
    image_url = agent.generate_image("A futuristic cityscape at night.")
    print(f"Generated Image URL: {image_url}")

    edited_image = edit_image("cityscape.png", "Add a glowing moon in the background.")
    print(edited_image)