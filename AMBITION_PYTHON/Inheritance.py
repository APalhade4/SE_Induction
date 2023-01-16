
''' INHERITANCE '''


'''================================================================================
        SINGLE-LEVEL INHERITANCE
================================================================================'''

class A: #--------------------------------> This is Parent class
    name = 'Ambition'
    year = '2022'

class B(A): #--------------------------------> This is Child class
    student = 13
    batch = '01'


obj = B() #--------------------------------> Always Object will be of Child class


'''================================================================================
        MULTI-LEVEL INHERITANCE
================================================================================'''


class A:
    name = 'Ambition'
    year = '2022'

class B(A):
    student = 13
    batch = '01'

class C(B):
    fees = 25000
    duration = '3 Months'

obj = C()



'''================================================================================
            MULTIPLE INHERITANCE
================================================================================'''

class A:
    name = 'Ambition'
    year = '2022'


class B:
    student = 13
    batch = '01'


class C(A,B):
    fees = 25000
    duration = '3 Months'


obj = C()



