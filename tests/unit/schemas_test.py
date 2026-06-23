import pytest
from app.schemas import UserCreate


def test_user_create_valid():
    user = UserCreate(email='test@example.com', password='strongpassword')
    assert user.email == 'test@example.com'
    assert user.password == 'strongpassword'


def test_user_create_invalid_email():
    with pytest.raises(ValueError):
        UserCreate(email='invalid_email', password='strongpassword')


def test_user_create_short_password():
    with pytest.raises(ValueError):
        UserCreate(email='test@example.com', password='short')