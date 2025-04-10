import unittest
import requests

class TestEndpoints(unittest.TestCase):
    BASE_URL = "http://localhost:5000"

    def test_home_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to NeuraMind AI Backend", response.text)

    def test_route_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/route")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Route from", response.text)

    def test_generate_image_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/generate-image")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Image generated successfully", response.text)

if __name__ == "__main__":
    unittest.main()
