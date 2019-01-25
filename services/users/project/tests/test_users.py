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
            "/users",
            data=json.dumps({"username": "savio", "email": "savio@gmail.com"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn("savio@gmail.com was added", data["message"])
        self.assertIn("success", data["status"])

    def test_add_user_invalid_json(self):
        """
        Missing email and username should raise Invalid data 
        """
        with self.client:
            response = self.client.post(
                "/users", data=json.dumps({}), content_type="application/json"
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            self.assertIn("Invalid data", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_invalid_json_keys(self):
        """Test that there should be a failure if there is a missing `email` key"""
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps({"username": "savio"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            self.assertIn("Invalid data", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_duplicate_email(self):
        """Test that there is a failure when the email is duplicate"""
        with self.client:
            self.client.post(
                "/users",
                data=json.dumps({"email": "savio@gmail.com", "usernmame": "savio"}),
                context_type="application/json",
            )
            response = self.client.post(
                "/users",
                data=json.dumps({"email": "savio@gmail.com", "usernmame": "savio"}),
                context_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            self.assertIn("Sorry. That email already exists", data["message"])
            self.assertIn("fail", data["status"])


if __name__ == "__main__":
    unittest.main()
