import pytest


# (XPASS)
@pytest.mark.xfail
def test_fact():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert name is message


@pytest.mark.xfail
def test_fact_001():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert name in message


def test_fact_002():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert not name in message


def test_fact_003():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert name in message