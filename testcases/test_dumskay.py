import pytest
from example1 import register_user
from example12 import register_user as wrong_password


def test_user_registration():
    a = register_user()
    assert a[0] == a[1]


def test_user_registration_wrong_password():
    a = wrong_password()
    assert a[0] == a[1]
