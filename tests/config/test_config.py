import pytest

@pytest.fixture(scope='session')
def db():
    # Setup database connection
    yield
    # Teardown database connection


def pytest_configure():
    pytest.db = db