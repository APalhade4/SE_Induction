import pytest


@pytest.mark.smoke
def test_verify_001():
    x = 10
    y = 20
    assert x == y


@pytest.mark.anurag
def test_verify_002():
    x = 10
    y = 20
    assert not x == y


@pytest.mark.anurag
def test_verify_003():
    x = 10
    y = 20
    assert x == y