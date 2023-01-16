

''' __init__ : '''

# It is a special methods in python called "Constructor"
# It can be only used with "Class"
# It is a reserved method in Python
# It will get automatically Called.


class Computer:
    def __init__(self, ram, cpu, process): # -------------> This is Constructor
        print("I am Init")
        self.ram = ram  # --------------------------------> this are the Variables
        self.cpu = cpu
        self.process = process

    def config(self): # ----------------------------------> This is Method
        print("My Config is : ", self.ram, self.cpu)

    def config_1(self):
        print("My Config is :", self.cpu)

    def config_2(self):
        print("My Config is :", self.process)

comp = Computer(16, 'i3', 'snapdragon')

comp.config()
comp.config_1()
comp.config_2()


