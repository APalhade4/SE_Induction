import pytest

# What is Fixtures:
    # It helps to reduce the code size
    # It helps to reuse the code in multiple function

# What is Yield:
    # It helps to run the code before and after

@pytest.fixture
def login_setup():
    print("webdriver.Chrome")
    print("do maximize")
    yield
    print("driver refresh page")
    print("driver close window")

def test_login_facebook(login_setup):
    print("driver.get Facebook.com")

def test_login_amazon():
    print("driver.get amazon.com")

def test_login_gmail(login_setup):
    print("driver.get gmail.com")

