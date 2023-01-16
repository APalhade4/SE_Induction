import pytest


@pytest.mark.parametrize('username, password',
                             [
                                 ('9529658851', 'Swami@123'),
                                 ('abc', 'sdaEdfC'),
                                 ('DVASCd', 'dvsfVS'),
                                 ('dfjn', 'eiydbc')
                             ]
                         )

def test_function(username, password):
    print(username + 'is owner of' + password)


