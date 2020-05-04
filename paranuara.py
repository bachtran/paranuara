import os
from app import create_app, db
from app.models import Person, Food, Company

"""App entry point"""

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    """Place database and models in shell context"""
    return dict(db=db, Person=Person, Company=Company, Food=Food)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def import_data():
    """Import data from resources/companies.json and resources/people.json"""
    import import_data
    import_data.run()
