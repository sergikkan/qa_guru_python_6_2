import pytest


@pytest.fixture
def user_id():
    return 123


def test_auth(user_id):
    assert user_id == 123
    pass
