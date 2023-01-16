

'''================================================================================
              SYNTAX ERROR
================================================================================'''

# As the name suggests this error is caused by the wrong syntax in the code.
# It leads to the termination of the program.

# i = 0
# if i = 0:
#  print(i)


'''================================================================================
              Exception
================================================================================'''

# Exceptions are raised when the program is syntactically correct but the code is results in Errors.
# This error does not terminate the execution of program,
# However, It changes the normal flow of the program.

# print(0 / 0)


'''================================================================================
              Try and Except Statements
================================================================================'''

# Ambition = [10, 20, 30]
# try:
#  print ("Second Element of Ambition is = " ,(Ambition[1]))
#  print("Fourth Element of Ambition is = ", (Ambition[3]))
#
# except:
#  print ("An Exception Occured")


'''================================================================================
              Try and Except Statements
================================================================================'''

# try:
#  n = int(input("Enter any number : "))
#  def factorial(n):
#      if n == 0 or n == 1 or n == 2 or n < 0:
#          return n
#      else:
#          return n*factorial(n / 0)
#
#  print(factorial(n))
#
# except ZeroDivisionError:
#  print("Value is not divisible by Zero")
#
# except NameError:
#  print("Value is not defined")
#
# except IndexError:
#  print("Enter a Correct Index Number")



'''================================================================================
              Try, Except, Else, and Finally Statements
================================================================================'''

try:
 n = int(input("Enter any number : "))
 def factorial(n):
     if n == 0 or n == 1 or n == 2 or n < 0:
         return n
     else:
         return n*factorial(b - 1)
 print(factorial(n))


except ZeroDivisionError:
 print("Value is not divisible by Zero")
except NameError:
 print("Value is not defined")
except IndexError:
 print("Enter a Correct Index Number")
except IndentationError:
    print("Enter a Correct Syntax")


else:
 print("An Exception Occurred")

finally:
 print("Program Executed")







