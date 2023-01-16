

"""
PYTHON Executes the code Line by Line
"""



# comment

'''comment'''
""" comment """

# Modules
# Built-in modules - e.g. os, math
# -------> Defined by Pyhton

# External Modules - e.g. flask



''' Variables '''

# anurag = 'Anurag is a engineer' # ----> Here Anurag is a Variable
# print(anurag)

''' Keyword '''
# Reserved words in Python, Python having total 26 Keywords
# True
# False
# is
# in

'''Identifiers'''
# class/function/variable name


""" DATA TYPES"""
# (int) Integer - 10,20,30, -10,-20
# (float) Float - 10.1, 20.5, -2.5, -96.3
# (str) Strings - 'anurag52356223palhade' or "anurag5@#@#@2356223palhade"
# (bool) Booleans - True/False
# None


# Rules for defining a variable name
# 1. A variable name can contain alphabets, digits, and underscore.
# someName123 = “hello”
# 2. A variable name can only start with an alphabet and underscore.
# 3. A variable can’t start with a digit.
# 4. No white space is allowed to be used inside a variable name.
# some_name = “Hello” #Valid
# some name = “hello” #invalid
# 5. Variable names are case sensitive

# anurag = 'Anurag is a Engineer.'
# anurag123 = 'Anurag is a Engineer.'
# anurag123_= 'Anurag is a Engineer.'
# anurag_123 = 'Anurag is a Engineer.'
# anurag-123 = 'Anurag is a Engineer.' #-----------------------> WRONG
# _anurag = 'éngjpfcem'
# 123anurag_ = 'jlNSCDNC' #-----------------------> WRONG
# anurag_123 = 'jsxnljsnx' #-----------------------> WRONG


"""
STRING CAN CONTAIN ANYTHING (ALPHABETS, NUMBERS and SPECIAL CHARACTER)
"""


""" TYPE FUNCTION"""
#
# a = 123
# b = 'anurag'
# c = 10.1


# print(type(a))
# print(type(b))
# print(type(c))
#
""" TYPE-CASTING """
#
 # a = str(123)
 # b = int('anurag') ------------------> HERE Typecasting is not possible, Because We never convert numbers into Alphabets
 # c = int(10.9)
#
 # print(type(a))
# print(type(c))
# # print(type(b))


""" PYTHON OPERATORS """
#
# 1. Arithmetic Operators (+, -, *, /, etc.)
# 2. Assignment Operators (=, +=, -=, *=, /=, etc.)
# 3. Comparison Operators (==, >=, <=, >, <, !=, etc.)
# 4. Logical Operators (and, or, not)


''' ARITHMETIC OPERATORS '''

# METHOD - 1
# a = 10
# b = 20
# c = a + b
# print(c)


# METHOD - 2
# a = 10 --------------------------------------> HARD CODING
# b = 20 --------------------------------------> HARD CODING
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


""" INPUT FUNCTION """

# a = int(input("Please enter any Number for a : ")) --------------> SOFT CODING
# b = int(input("Please enter any Number for b : ")) --------------> SOFT CODING

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# a = input ('Énter your name: ')
# print("Hello Mr.", a)

# a = 9.5
#
# print (a*1)
# print (a*2)
# print (a*3)
# print (a*4)
# print (a*5)
# print (a*6)
# print (a*7)
# print (a*8)
# print (a*9)
# print (a*10)

# name = input('please enter name: ')
# surname =input('please enter surname: ')
# print (name , surname)


""" STRING Slicing"""

# a = 'anuragpalhade'
# b = a[2:9] #=====> Length = 4, whenever you will get O/p which will be Length - 1
# print(b)
#
# a = 'anurag'
# b = a[-4:-2]
# print(b)

#  a n u a r g a n u r a g
# -6-5-4-3-2-1 0 1 2 3 4 5


""" STRING """
# String can contain anything: Alphabets, Numbers and Special characters
# 'anurag123@gmail.com' OR "anurag123@gmail.com"

""" LENGTH function of String """

# a = "Anuragpa"
# print(len(a))

""" ENDSWITH function of String """
# a = "Anuragpa"
# print(a.endswith('gpa')) #---------> True
# print(a.endswith('rag')) #---------> False

""" COUNT function of String """

# b ="ShanT123anu"
#
# print(b.count('a'))
# c = b.casefold()
# d = b.lower()
# e = b.upper()
# f = b.capitalize()
# print(b.isdigit())
# h = b.isalnum()
# print(h)


# """ LIST """
# list = [10, 20, 'Anurag', 10.5, 10, 20, 20, 10]
#
# """ LIST INDEXING """
# # Finding the position using INDEX value
# print(list[2])

# # """ LIST SLICING """
# c = list[0:2]
# print(c)

# print(list.count(20))

# a = 'shweta_palhade123'
# b = a[2:9]
# print(type(b))


# list = [10, 20, 10, 20, 40, 30, 10.5] ----------------------> Ascending
# list.sort()
# print(list)

# list = ['anurag', 'shweta', 'shantanu']
# list.sort()
# print(list)


# list = [10, 20, 10, 20, 40, 30, 10.5] #-------------------------> As is it reverse
# list.reverse()
# print(list)
#
# list.append(8)
# print(list)

# list = [10, 20, 10, 20, 40, 30, 10.5, 40, 40, 40]
# list.insert(3, 9)
# list.pop(4) #------------------------------------> It works as a delete
# list.sort()
# list.remove(40)
# print(list)


# shweta = (20,30,10,40,50,10,80)
# a = shweta.count(10)
# print(a)
#
# b = shweta.index(10)
# print(b)

# a = 'shweta is a good girl'
# b = [a]
# b.reverse()
# print(b)


# QUE: Find length of a string
# my_string = 'Hello'
# print(len(my_string))

# Input = 'shweta is a 12good gi5679rl'
# print(Input.isdigit())

# Input = 'SHWETA'
# print(Input.isdigit())
# print(Input.lower())

# string ==='' or ""
# list === []
# tuple === () or empty
# dictionary === {'key':'Value'}
# set{1,2,3,4}

"""" DICTIONARY """

# Dictionary = {'anurag_palhade' : 9595159191, 'book': 78952136, 'book' : 12345, 'shweta':123, 'shantanu' : 456123, 'anurag_palhade_1' : 9595159191}
# unordered ---->
# Unindexed ---->
# It is indexed by Key
# It will not accept duplicate key but accept Duplicate Value.


# a = {"key" : "value",
# "harry": "code",
# "marks" : "100",
# "list": "123456"}
# b = a.keys()
# print(b)
# c = a.get('harry')
# print(c)
# a.update({"list":'123'})
# print(a)
# print("This is Original Dict: ", a)
# a.update({"list":'123'})
# print("This is Updated Dict: ", a)
# e = a.items()
# print(e)

""" SET """

# DEFINATION:  Set is a collection of non-repetitive elements (No Duplicates Allowed)
    # Sets are unordered # Elements order doesn’t matter
    # Sets are unindexed # Cannot access elements by index
    # There is no way to change items in sets - Immutable items (Cannot change value)
    # Set is as whole mutable but inside items are immutable
    # Sets cannot contain duplicate values
    # Add multiple elements in set by passing them as a tuple

# sets = {10, 20, 30, 40, 20, 50, 10}
# sets.update((80, 70, 60)) #----------------------------> It will insert multiple values
# sets.add(100) #----------------------------> It will insert EXACTLY one value
# print(sets)

# anu = {1, 2, 3, 4, 5}
# rag = {6, 7, 8, 1}

# b = anu.pop()
# print(b)
# print(anu)
#
# b = anu.union({9, 7})
# print(b)



""" CONDITIONAL EXPRESSION """

# -- IF
# -- ELIF (Optinal)
# -- ELSE


# a = int(input("enter any number: "))
# if a > 100:
#     print("Hello Anurag")
# elif a == 10:
#     print("Hello shweta")
# else:
#     print("Invalid number")



""" LOOPS """

"***** WHILE LOOP *****"
#
# i = 0
# while i < 5: # condition to be checked on every iteration
#     print("Hello")
#     i = i+1
# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello
# 5--- Execution stoped

# Loops are used to iterate a code. It will execute util condition became false.



"***** FOR LOOP *****"

# anurag = "anurag palhade"
# for i in anurag:
#     print(i)


"***** RANGE FUNCTION *****"
# for shweta in range(1,100):
#     print(shweta)


# a = int(input("Enter any number: "))
# if a < 15:
#     print("Please enter Number greater than 15")
# else:
#     for i in range(1, a):
#         print(i)


"***** FOR LOOP With ELSE*****"

# anurag = "anurag palhade"
# for i in anurag:
#     print(i)
# else:
#     print("Done")


"***** Function *****"

# def func():
#     anurag = "anurag palhade"
#     for i in anurag:
#         print(i)
#
#     i = 0
#     while i < 5:  # condition to be checked on every iteration
#         print("Hello")
#         i = i + 1
# print(func())


"***** Function with Arguments *****"

# def greet(name: str) -> str:
#     palhade = "Hello, My name is " + name
#     return palhade
#
# print(greet('anurag'))


''' What is the difference between Print and Return '''
''' What is the difference between Iteration and Recursion '''

# Teration = Infinite
# Recursion = 1000 Times


''' Write doen the program for Factorials '''

# n = int(input("Enter any number : "))
# def factorial(n):
#     if n == 0 or n == 1 : #Base condition which doesn’t call the function any further
#         return n
#     else:
#         return n*factorial(n-1) #Function calling itself
#
# print(factorial(n))












