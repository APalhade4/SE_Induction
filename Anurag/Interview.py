
# string = 'My name isa pythona'
# string_1 = string[::-1]
# print(string_1)
# print(string.count('a'))

# mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
# print("The position of Tutorials is at:", mystring.find("Tutorials", 20))

# new_string = string.split()
# print("The splitted string is as follow: ", new_string)

# string = '123'
# string_1 = string.isdigit()
# print(string_1)

# string = "I am a python programmer"

# words = string.split()
# print("Splitting : ", words)
# words.reverse()
# print("Reversing : ", words)
# print(" ".join(words))

# string = '  My name is pythona  '
# string_1 = string.replace('pythona', 'python', 2)
# print(string_1)
# a = string.strip()
# print("Original String : ", string)
# print("Stripped String : ", a)

# lists = [10, 20, 30, 'Ambition', 10.75, False, 10, None]
# a = lists.index(10.75, 0, 5)
# print(a)

# b = lists[0:2]
# print(b)

# c = lists.count(10)
# print(c)

# list.extend(set)
# print(list)

# lists.reverse()
# print(lists)

# lists.clear()
# lists.extend([50, 20])
# print("Extended List : ", lists)
# lists.append([50,20])
# print("Appended List : ", lists)

# lists.pop(5)
# print("popped List : ", lists)

# lists.insert(5, True)
# print("Inserted List : ", lists)

# new_list = lists.copy()
# print("Copied List   : ", new_list)


# tuples = ('Anurag', 10, 20.35, True, None, 10, 10)
# a = tuples.count(10)
# print(a)

# b = tuples.index(10, 2)
# print(b)


a = {"key" : "value", "harry": "code", "marks" : "100", "list": '12'}
# print(lists)
#
# a.pop('list')
# print(a)
#
# c = a.get('marks')
# print(c)
#
# a.update({'Anurag':'Shweta', 'Raja':'Rani'})
# print(a)


# a = {'Mumbai', 'Bangalore', 'Delhi'}
# b = 'City'
# c = dict.fromkeys(a,b)
# print(c)
#
# a = {"key" : "value", "harry": "code", "marks" : "100", "list": '12'}
# b = a.pop('harry')
# print(b)
#
# a.popitem()
# print(a)

# a = {"key" : "value", "harry": "code", "marks" : "100", "list": '12'}
# b = a.values()
# print(a)

# car = {
#   "brand": "Ford",
#   "model": '',
#   "year": 1964
# }
#
# x = car.setdefault(" anurag ", "Bronco")
#
# print(car)



# class A:
#
#     def display(self, name='', lastname=''):
#         print('Hello', 'World', name, lastname)
#
# obj = A()
#
# obj.display()
# obj.display('Ambition')
# obj.display('Ambition', 'Institute')




# print("Enter number")
# number = int(input())
# fac = 1
# if number == 0:
#   print (1)
# else:
#   while number > 1:
#     fac = fac*number
#     number = number-1
#     print (number)
#   print(fac)


# a = [2, 3, 4, 5]
# b = []
# for i in a:
#     b.append(i**2)
#
# print(b)
#
#
# even = []
# odd = []
#
# for i in range(1,101):
#   if i%2 == 0:
#     even.append(i)
#   else:
#     odd.append(i)
#
# print(even)
# print(odd)



# l = [1, 7, 8, 9, 12, 15, 21, 87]
#
# for item in range(10):
#
#     if item == 5:
#         continue
#     print("The Number is :", item)




# for i in range(1, 20):
#     print(i)
# else:
#     print("Done")




# num = (1,2,3,4,5,6,7,8)

# for i in num:
#     print(i)
#     if i == 4:
#         break

# count = 0
# while (count<9):
#   print (num[count])
#   count = count+1
#   if count == 4:
#      break

#
# for letter in 'Python':     # First Example
#    if letter == 'h':
#       pass
#    print('Current Letter :', letter)

# li = ['a', 'b', 'c', 'd']
# li = 'a', 'b', 'c', 'd'
# for i in li:
#     if (i == 'b'):
#         pass
#     else:
#         print(i)

#
# def func1():
#    print("Hello")  # function body # function code
#
#
# def greet(name):
#    gr = "Hello" + ' ' + name
#    return gr
# print(greet("Credence"))

# n = 9 #int(input("ENter any Number : "))
# def factorial(n):
#    if n == 0 or n == 1:  # Base condition which doesn’t call the function any further
#       return n
#    else:
#       print(n)
#       return n * factorial(n-1)



n = int(input("Enter any number : "))
def fibonacci(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * fibonacci(n -1)

print(fibonacci(n))








