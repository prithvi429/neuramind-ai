from flask import Flask
from nav_agent import get_route
from image_agent import generate_image

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to NeuraMind AI Backend!"

@app.route("/route")
def route():
    # Example route calculation
    return get_route("New York", "Los Angeles")

@app.route("/generate-image")
def generate_image_route():
    # Example image generation
    return generate_image("A futuristic cityscape at night.")

if __name__ == "__main__":
    app.run(debug=True)
