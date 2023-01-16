


# dictionary = {'key' : 'value'}

# ==    # This is used for comparison

#  =     # this is used to create Variable (assigning value)


'''================================================================================'''

# class Ambition:   #------------------------------> Creating or Defining Class
#     def Method_1(self):
#         print("I am Learing Python")
#
#     def Method_2(self):
#         print("I am Learing Python-Selenium")

# variable = Ambition() #------------------------------> Creating Object for Class
#
# variable.Method_2() #------------------------------> Calling function of Class

'''================================================================================
            Class and Object
================================================================================'''

# class Ambition_2:
#     def Extra_1(self):
#         print("I am Learing Python")
#
#     def Extra_2(self):
#         print("I am Learing Python-Selenium")
#
# class Ambition_3:
#     def Fun_1(self):
#         print("I am Learing Python")
#
#     def Fun_2(self):
#         print("I am Learing Python-Selenium")


'''================================================================================
        INHERITANCE
================================================================================'''

# Single-Level Inheritance
#
# class A:
#     def classA(self):
#         print("I am Property of Class-A")
#
#     def objectsA(self):
#         print("I am Property of Class-A")
#
#     def functionsA(self):
#         print("I am Property of Class-A")
#
# class B(A):
#     def classB(self):
#         print("I am Property of Class-B")



# Multi-Level Inheritance

# class A:
#     def classA(self):
#         print("I am Property of Class-A")
#
# class B(A):
#     def classB(self):
#         print("I am Property of Class-B")
#
# class C(B):
#     def classC(self):
#         print("I am Property of Class-C")


# Multiple Inheritance

# class Parent:
#     def Mobile(self):
#         print("My Dad Have Mobile")
#
# class Shantanu(Parent):
#     def Mobile(self):
#         print("I Have Mobile - Iphone: 14")
#
#
# object = Shantanu()
# object.Mobile()



# 12th ----------> No Mobile --------> I dont have mobile
# 12th ----------> No Mobile --------> I dont have mobile
# 12th ----------> No Mobile --------> My Dad have mobile (Iphone 14)

'''================================================================================
        INHERITANCE
================================================================================'''

''' OverRiding'''

# 12th ----------> I have mobile (Iphone 14)

# class Parent:
#     def Mobile(self):
#         print("My Dad Have Mobile")
#
# class Shantanu(Parent):  # --------------> Child Class
#     def Mobile(self):
#         print("I Have Mobile - Iphone: 14")


''' Over-Loading'''

# class A:
#     def Movie(self, name='', date=''):
#         print("My Movie name is : ", name, date)
#
# object = A()
# object.Movie('Kantara', '10-10-22')



""" __init__"""

# It is a Constructor


# class Ambition:
#     def __init__(self, name: str, number: int) -> bool:
#         self.name = name
#         self.number = number
#
#     def function_1(self):
#         print("My name is : ", self.name)
#
#     def function_2(self):
#         print("My name is : ", self.number)
#
#     def function_3(self):
#         print("My name is : ", self.name, self.number)

# object = Ambition()
# object.function_1()
# object.function_2()
# object.function_3()

# def logic(self, name):
#     print("Show Logic", name)
#
# logic('Shekhar')

# class Metadata:
#     def logic(self, name):
#         print("Show Logic", name)

# object = Metadata()
# object.logic('Ambition') #-------------------> Here we are calling function through Object

# Metadata.logic("Show Logic",'Swapnil') # ------> Here we are calling function through class (We have to provide all the arguments while calling fuction)



'''================================================================================
              Write a Program for Factorial
================================================================================'''

# n = int(input("Enter any number : "))
# n = 5
# def Factorial(n):
#     if n == 0 or n == 1 or n == 2:
#         return n
#     else:
#         return n*Factorial(n-1)
#
# print(Factorial(n))


'''================================================================================
              Write a Program for finding Prime-Number
================================================================================'''

n = int(input("Enter any Number : "))
if n > 1:
    for i in range(2 , n):
        if n % i == 0:
            print(f"{n} is Not a Prime Number")
            break
    else:
        print(n, "is a Prime Number")
else:
    print(f"{n} is Not a Prime Number")


'''================================================================================
              Write a Program to print Prime-Number from 0 to 50
================================================================================'''





'''================================================================================
              Write a Program to find Even-Odd Number
================================================================================'''





'''================================================================================
Write a Program and store Even Numbers is seperate list and Odd Numbers is seperate list
================================================================================'''





