# Methods:
     # Instance Method
     # Class Method
     # Static Method


# Static Method:
    # It is a general utility method that perform a task in ISOLATION.
    # Inside this method, we don't use instance or class variable
        # bacause this static method doent take any parameter like SELF or CLS


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

    @staticmethod
    def method_info(age):
        return age > 12


@staticmethod
def method_info(age):
    return age > 12


s1 = School(10, 20, 50)
s2 = School(50, 60, 90)
print(s1.average()) # -----------------> Instance Method
print(s2.average())


print(School.class_info()) # ----------> @classmethod


print(School.method_info(10)) # ----------> @staticmethod
print(method_info(10)) # -----------------> @staticmethod








