import unittest
from app import app # Import the Flask app from your main application file (app.py)

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up test client for the Flask App
        self.app = app.test_client()
        self.app.testing = True # Enable Testing Mode

    def test_welcome(self):
        # Send get request to the root url.
        response = self.app.get('/')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected message
        self.assertEqual(response.get_json(), {"message": "You are Welcome!"})

if __name__ == '__main__':
    unittest.main()

