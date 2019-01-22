import json
import unittest
from project.tests.base import BaseTestCase


class TestUserTestCase(BaseTestCase):
    def test_ping_pont(self):
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assert200(response)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])


if __name__ == "__main__":
    unittest.main()
