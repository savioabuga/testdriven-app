import unittest
from sqlalchemy.exc import IntegrityError

from project.api.models import User
from project.tests.utils import add_user
from project import db
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user(username="justatest", email="test@test.com", password="samsung")
        self.assertTrue(user.id)
        self.assertEqual(user.username, "justatest")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.active)

    def test_adding_duplicate_username(self):
        add_user(username="justatest", email="test@test.com", password="samsung")
        duplicate_user = User(
            username="justatest", email="test@test2.com", password="samsung"
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_adding_duplicate_email(self):
        add_user(username="justatest", email="test@test.com", password="samsung")
        duplicate_user = User(
            username="justatest1", email="test@test.com", password="samsung"
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_jsons(self):
        user = add_user(username="justatest", email="test@test.com", password="samsung")
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        user_one = add_user(
            username="savio1", email="savio1@gmail.com", password="samsung"
        )
        user_two = add_user(
            username="savio2", email="savio2@gmail.com", password="samsung"
        )
        self.assertNotEqual(user_one.password, user_two.password)

    def test_add_user(self):
        user = add_user(username="savio1", email="savio1@gmail.com", password="samsung")
        self.assertEqual(user.username, "savio1")
        self.assertEqual(user.email, "savio1@gmail.com")
        self.assertTrue(user.password)
        self.assertTrue(user.active)
        self.assertTrue(user.id)


if __name__ == "__main__":
    unittest.main()
