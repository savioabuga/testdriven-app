import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import User
from project.tests.utils import add_user
from project import db


class TestUserTestCase(BaseTestCase):
    def test_ping_pont(self):
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assert200(response)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])

    def test_add_user(self):
        add_user("test", "test@test.com", "test")
        resp_login = self.client.post(
            "/auth/login",
            data=json.dumps({"email": "test@test.com", "password": "test"}),
            content_type="application/json",
        )
        token = json.loads(resp_login.data.decode())["auth_token"]
        response = self.client.post(
            "/users",
            data=json.dumps(
                {"username": "savio", "email": "savio@gmail.com", "password": "samsung"}
            ),
            content_type="application/json",
            headers={"Authorization": f"Bearer {token}"},
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn("savio@gmail.com was added", data["message"])
        self.assertIn("success", data["status"])

    def test_add_user_invalid_json(self):
        """Missing email and username should raise Invalid data"""
        add_user("test", "test@test.com", "test")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "test"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.post(
                "/users",
                data=json.dumps({}),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            self.assertIn("Invalid payload", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_invalid_json_keys(self):
        """Test that there should be a failure if there is a missing `email` key"""
        add_user("test", "test@test.com", "test")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "test"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.post(
                "/users",
                data=json.dumps({"username": "savio", "password": "test"}),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            self.assertIn("Invalid payload", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        add_user("test", "test@test.com", "test")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "test"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            self.client.post(
                "/users",
                data=json.dumps(
                    {
                        "username": "michael",
                        "email": "michael@mherman.org",
                        "password": "samsung",
                    }
                ),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            response = self.client.post(
                "/users",
                data=json.dumps(
                    {
                        "username": "michael",
                        "email": "michael@mherman.org",
                        "password": "samsung",
                    }
                ),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Sorry. That email already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user(self):
        user = add_user(
            username="savio", email="savioabuga@gmail.com", password="samsung"
        )
        with self.client:
            response = self.client.get(f"/users/{user.id}")
            data = json.loads(response.data.decode())
            self.assert200(response)
            self.assertIn("savio", data["data"]["username"])
            self.assertIn("savioabuga@gmail.com", data["data"]["email"])
            self.assertIn("success", data["status"])

    def test_single_user_no_id(self):
        """Ensure error is thrown if no id provided """
        with self.client:
            response = self.client.get("/users/blah")
            self.assert404(response)
            data = json.loads(response.data.decode())
            self.assertIn("User does not exist", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if there is no id """
        with self.client:
            response = self.client.get("/users/blah")
            self.assert404(response)
            data = json.loads(response.data.decode())
            self.assertIn("User does not exist", data["message"])
            self.assertIn("fail", data["status"])

    def test_get_all_users(self):
        add_user(username="savio", email="savioabuga@gmail.com", password="samsung")
        add_user(username="joseph", email="joseph@gmail.com", password="samsung")
        with self.client:
            response = self.client.get("/users")
            data = json.loads(response.data.decode())
            self.assert200(response)
            self.assertEqual(len(data["data"]["users"]), 2)
            self.assertEqual("savio", data["data"]["users"][0]["username"])
            self.assertEqual("joseph", data["data"]["users"][1]["username"])
            self.assertEqual("savioabuga@gmail.com", data["data"]["users"][0]["email"])
            self.assertEqual("joseph@gmail.com", data["data"]["users"][1]["email"])

    def test_main_no_users(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assertIn(b"All Users", response.data)
        self.assertIn(b"<p>No users!</p>", response.data)

    def test_main_with_users(self):
        add_user(username="savio", email="savioabuga@gmail.com", password="samsung")
        add_user(username="joseph", email="joseph@gmail.com", password="samsung")
        with self.client:
            response = self.client.get("/")
            self.assert200(response)
            self.assertIn(b"All Users", response.data)
            self.assertNotIn(b"<p>No users!</p>", response.data)
            self.assertIn(b"joseph", response.data)
            self.assertIn(b"savio", response.data)

    def test_main_add_user(self):
        with self.client:
            response = self.client.post(
                "/",
                data=dict(username="seba", email="seba@gmail.com", password="samsung"),
                follow_redirects=True,
            )
            self.assertIn(b"All Users", response.data)
            self.assertNotIn(b"<p>No users!</p>", response.data)
            self.assertIn(b"seba", response.data)

    def test_add_user_invalid_json_keys_no_password(self):
        """Ensure that error is thrown if there is no password in JSON key"""
        add_user("test", "test@test.com", "test")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "test"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.post(
                "/users",
                data=json.dumps({"username": "savio", "email": "savio@andel.com"}),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_not_admin(self):
        add_user("test", "test@test.com", "test")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "test"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.post(
                "/users",
                data=json.dumps({"username": "savio", "email": "savio@andel.com"}),
                content_type="application/json",
                headers={"Authorization": f"Bearer {token}"},
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTemplateUsed(data["message"] == 'You do not have permission to do that.')
            self.assertIn("fail", data["status"])


if __name__ == "__main__":
    unittest.main()
