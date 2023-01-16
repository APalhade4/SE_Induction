# Methods:
     # Instance Method
     # Class Method
     # Static Method


# Class Method:
    # This instance method used to acess of modify the object state.
    # In method implementation, If we use only a class veriables, then
            # such type of methods we should declare as a class method.
    # It must have a CLS parameter to refer to current class.
    # We are using @classmethod to define this method.


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

    @classmethod
    def class_info(cls):
        return cls.name, cls.count

s1 = School(10, 20, 50)
s2 = School(50, 60, 90)
print(s1.average())
print(s2.average())


print(School.class_info())
