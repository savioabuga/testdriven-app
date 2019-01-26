import unittest
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("seed_db")
def seed_db():
    """seeds db"""
    db.session.add(User(username="michael", email="hermanmu@gmail.com"))
    db.session.add(User(username="michaelherman", email="michael@mherman.org"))
    db.session.commit()


@cli.command()
def test():
    """runs tests"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command("recreate_db")
def recreate_db():
    """recreates dbs"""
    db.drop_all()
    db.create_all()
    db.session.commit()  # noqa


if __name__ == "__main__":
    cli()
