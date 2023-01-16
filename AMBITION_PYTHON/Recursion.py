

'''==========================This is Iterative Method========================'''
# n = 2
# while n > 1 :
#     print(n)
#     n = n + 1

'''==========================This is  Calling Method =========================='''

# def method(name):
#     print("Hello World", name)
# method('Anurag Palhade')          # ---------------> Calling Method


'''================================================================================
        RECURSION
============================This is Recursive Method============================'''


# Recursion is a process which calls itself.
# By default, the maximum depth of recursion is 1000
# recursion required memory

# def countdown(n):
#     print(n)
#     countdown(n + 1)
# countdown(1)

'''================================================================================
              Write a Program for Factorial
================================================================================'''

# n = int(input("Enter any number : "))
# def factorial(n):
#     if n == 0 or n == 1 or n == 2 or n < 0:
#         return n
#     else:
#         return n*factorial(n - 1)
#
# print(factorial(n))