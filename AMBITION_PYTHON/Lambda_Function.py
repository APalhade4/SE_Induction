
# Lambda is a function which supports single line statement that returns some values.
# It is a special function
# Also known as Anonymous Function
# Syntax =
    # Function = lambda Argument : Expression

''' Using Normal Function'''
# def add():
#     a = 10
#     b = 20
#     return a + b
# print(add())

''' Using Lambda Function'''
# add = lambda a, b : a + b
# print(add(10, 20))


""" ================================================================ """

''' Using Normal Function'''
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(30, 20))

''' Using Lambda Function'''

# max = lambda a, b : a if (a > b) else b
# print(max(30, 20))

"""===================================================================================
Write a code for Capitalization of string and and also reverse that string
==================================================================================="""

''' Using Normal Method '''

# string = "We are learning python"
# str = string.upper()
# reverse = str[::-1]
# print(reverse)

''' Using Lambda Function '''

# reverse_1 = lambda string : string.upper()[::-1]
# print(reverse_1("We are learning python"))


""" ================================================================
Write a code to perform addition of two list using Lambda function
================================================================ """

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
#
# Result = map(lambda x, y : x + y, list_1, list_2)
# print(list(Result))


# Expected Output = [5, 7, 9]
# webpage.title == facebook.com;
# assert (lambda login : abc if webpage.title == facebook.com else xyz)


