from backend.image_agent import generate_image

def main():
    """
    Runs the image generation agent with an example prompt.
    """
    prompt = "A futuristic cityscape at night."
    result = generate_image(prompt)
    print(result)

if __name__ == "__main__":
    main()
