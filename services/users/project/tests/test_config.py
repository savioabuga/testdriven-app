import unittest
import os
from project import create_app
from project.tests.base import BaseTestCase

app = create_app()


class TestDevelopmentConfig(BaseTestCase):
    def create_app(self):
        app.config.from_object("project.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_precious")
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
        )
        self.assertTrue(app.config["DEBUG_TB_ENABLED"])
        self.assertEqual(app.config["BCRYPT_LOG_ROUNDS"], 4)


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
        self.assertFalse(app.config["DEBUG_TB_ENABLED"])
        self.assertEqual(app.config["BCRYPT_LOG_ROUNDS"], 4)


class TestProductionConfig(BaseTestCase):
    def create_app(self):
        app.config.from_object("project.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_precious")
        self.assertFalse(app.config["TESTING"])
        self.assertFalse(app.config["DEBUG_TB_ENABLED"])
        self.assertEqual(app.config["BCRYPT_LOG_ROUNDS"], 13)


if __name__ == "__main__":
    unittest.main()
