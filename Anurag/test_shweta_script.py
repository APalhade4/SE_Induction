
import pytest

def test_machine():
    a = int(input("Enter Any Number: "))
    if a > 10:
        print("Number is greater")
    else:
        print("Smaller")

def test_mt12():
    a = int(input("Enter Any Number: "))
    if a > 10:
        print("Number is greater")
    else:
        print("Smaller")


# @pytest.mark.regress
# def test_1():
#     x=10
#     y=20
#     assert x == y
#
# @pytest.mark.smoke
# def test_2():
#     x=10
#     y=20
#     assert x == y
#
# @pytest.mark.regress
# def test_3():
#     x = 10
#     y = 20
#     assert x == y
#
# @pytest.mark.smoke
# def test_4():
#     x = 10
#     y = 20
#     assert x == y


# # It is used to make code reusable.
#
# @pytest.fixture()
# def test_4():
#     x = 10
#     y = 20
#     assert x == y
#

