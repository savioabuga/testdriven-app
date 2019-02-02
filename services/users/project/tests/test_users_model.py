import unittest
from sqlalchemy.exc import IntegrityError

from project.api.models import User
from project.tests.utils import add_user
from project import db
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user(username="justatest", email="test@test.com")
        self.assertTrue(user.id)
        self.assertEqual(user.username, "justatest")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.active)

    def test_adding_duplicate_username(self):
        add_user(username="justatest", email="test@test.com")
        duplicate_user = User(username="justatest", email="test@test2.com")
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_adding_duplicate_email(self):
        add_user(username="justatest", email="test@test.com")
        duplicate_user = User(username="justatest1", email="test@test.com")
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_jsons(self):
        user = add_user(username="justatest", email="test@test.com")
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == "__main__":
    unittest.main()
