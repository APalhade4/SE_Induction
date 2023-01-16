# Methods:
     # Instance Method
     # Class Method
     # Static Method


# Instance Method
    # This instance method used to acess of modify the object state.
    # If we use instance veriable inside a method, such methods are Instance methods
    # It must have a SELF parameter to refer to current object.

class School:
    name = "Oxford"
    count = "13000"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        value = 1500
        summury = "Good University"
        return (self.m1 + self.m2 + self.m3)/3

s1 = School(10,20,50)
s2 = School(50, 60, 90)

print(s1.average())
print(s2.average())










