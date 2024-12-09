import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, CI/CD with Canary Deployment!", response.data)

if __name__ == "__main__":
    unittest.main()
