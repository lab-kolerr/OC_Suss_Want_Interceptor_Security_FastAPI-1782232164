import pytest
from app.models import User

@pytest.fixture
def user():
    return User(email='test@example.com', hashed_password='hashed_password')


def test_user_creation(user):
    assert user.email == 'test@example.com'
    assert user.hashed_password == 'hashed_password'


def test_user_email_uniqueness(user):
    assert user.email != 'duplicate@example.com'