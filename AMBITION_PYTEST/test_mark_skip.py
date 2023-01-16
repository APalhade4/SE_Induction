import pytest

@pytest.mark.skip(reason="The bug has been raised for this case")
def test_verify_001():
    x = 10
    y = 20
    assert x == y


@pytest.mark.skip(reason="Dont want to execute")
def test_verify_002():
    x = 10
    y = 20
    assert not x == y

def test_verify_005():
    x = 10
    y = 20
    assert not x == y


def test_verify_004():
    x = 10
    y = 20
    assert not x == y


@pytest.mark.skip
def test_verify_003():
    x = 10
    y = 20
    assert not x == y