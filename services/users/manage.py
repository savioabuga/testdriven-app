import unittest
from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)


@cli.command()
def test():
    """runs tests"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def recreate_db():
    """recreates dbs"""
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
