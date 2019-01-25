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

    def test_add_user(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"username": "savio", "email": "savio@gmail.com"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn("savio@gmail.com was added", data["message"])
        self.assertIn("success", data["status"])


if __name__ == "__main__":
    unittest.main()
