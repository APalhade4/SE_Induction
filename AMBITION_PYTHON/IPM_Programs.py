

'''================================================================================
        Write a Program to Print Factorial Number
================================================================================'''

# n = 10
# def Factorial(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * Factorial(n - 1)

# print(Factorial(n))


'''================================================================================
        Write a Program to Print FIBONACCI Sequence Number for 
================================================================================'''

# def fibonacci(n):
#     if n == 0 or n == 1 or n == 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci( n - 2)
# print(fibonacci(10))

'''================================================================================
        Write a Program to Display FIBONACCI Sequence Series
================================================================================'''

def fibo(n):
    if n < 0 or n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))

n1 = 12
if n1 <= 0:
    print("Valid Number")
else:
    for i in range(n1):
        print(fibo(i))







