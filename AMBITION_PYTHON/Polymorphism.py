
''' POLYMORPHISM'''

# POLY = MANY
# MORPHI = FORM

# It has a ability to take many forms


# class A:
#     def display(self):
#         print("Welcome")
#
#     def display(self, Firstname=''):
#         print("Welcome", Firstname)
#
#     def display(self, Firstname='', Lastname=''):
#         print("Welcome", Firstname, Lastname)
#
# obj = A()
#
# obj.display()
# obj.display('Ambition')
# obj.display('Ambition', 'Institute')

"OVER-LOADING"
# "OVERRIDING"
#     # Whenever we are creating a method name with same parameter in
#     # Parent and Child class called as "METHOD OVERRIDING"
#     # Inheritance is Mandatory for Overriding

# class A(object):
#     def __init__(self):
#         val = 98
#     def show(self):
#         print("Method defined in A")


# class B(A):
#     def __init__(self):
#         an_val = 75
#     def show(self):
#         print("Method defined in B")
#     def bar(self):
#         self.show()
#         super(B,self).show()


# obj = B()
# obj.show()
# obj.bar()


# class parent:
#     def mobile(self):
#         print("I dont have but My Parent have a Mobile")
#
# class sanket(parent):
#     def mob_1(self):
#         pass
#
#     def mobile(self):
#         print("I have iPHONE-14 PRO")
#         super(sanket, self).mobile()  # ---------------------> This is Seperate Function. This is not Overriding


# "OVERRIDING"
#     # Whenever we are creating a method name with same parameter in
#     # Parent and Child class called as "METHOD OVERRIDING"
#     # Inheritance is Mandatory for Overriding

