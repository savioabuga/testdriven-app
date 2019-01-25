import unittest
import os
from project import create_app
from project.tests.base import BaseTestCase

app = create_app()


class TestConfigTestCase(BaseTestCase):
    def create_app(self):
        app.config.from_object("project.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertEqual(app.config["SECRET_KEY"], "my_precious")
        self.assertTrue(app.config["TESTING"])
        self.assertEqual(
            app.config["SQLALCHEMY_DATABASE_URI"], os.environ.get("DATABASE_TEST_URL")
        )


if __name__ == "__main__":
    unittest.main()
