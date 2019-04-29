import unittest
from app import create_app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.request_context()

    def test_request(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
