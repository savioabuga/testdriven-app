import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import User
from project import db


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
            self.assertIn("Invalid payload", data["message"])
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
            self.assertIn("Invalid payload", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                "/users",
                data=json.dumps(
                    {"username": "michael", "email": "michael@mherman.org"}
                ),
                content_type="application/json",
            )
            response = self.client.post(
                "/users",
                data=json.dumps(
                    {"username": "michael", "email": "michael@mherman.org"}
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Sorry. That email already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user(self):
        user = User(username="savio", email="savioabuga@gmail.com")
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.client.get(f"/users/{user.id}")
            data = json.loads(response.data.decode())
            self.assert200(response)
            self.assertIn("savio", data["username"])
            self.assertIn("savioabuga@gmail.com", data["email"])
            self.assertIn("success", data["status"])

    def test_single_user_no_id(self):
        """Ensure error is thrown if no id provided """
        with self.client:
            response = self.client.get("/users/blah")
            self.assert404(response)
            data = json.loads(response.data.decode())
            self.assertIn("User does not exist", data["message"])
            self.assertIn("fail", data["status"])


if __name__ == "__main__":
    unittest.main()
