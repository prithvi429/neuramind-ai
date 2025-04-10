import unittest
from backend.nav_agent import get_route

class TestNavAgent(unittest.TestCase):
    def test_get_route(self):
        start = "New York"
        end = "Los Angeles"
        result = get_route(start, end)
        self.assertIn("Route from New York to Los Angeles", result)

if __name__ == "__main__":
    unittest.main()
