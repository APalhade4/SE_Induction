import pytest


@pytest.mark.skip
def test_fact():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert name in message


@pytest.mark.skipif(True, reason='The bug has been raised for this case')
def test_fact_001():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert name in message


def test_fact_002():
    name = 'Ambition'
    message = 'Ambition is a good place to learn Software testing'
    assert not name in message

