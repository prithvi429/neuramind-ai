import unittest
from selenium import webdriver

class TestFrontendRender(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homepage_render(self):
        self.driver.get("http://localhost:3000")
        self.assertIn("Welcome to NeuraMind AI", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
