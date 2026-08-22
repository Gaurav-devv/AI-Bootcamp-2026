#Encapsulation

#ACCESS MODIFIERS

#1.PUBLIC ATTRIBUTES AND METHODS

class Factory:
    a = "pune"

    def show(self):
        print("hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super().a)

obj = Bhopal()
obj.show2()


#2.PROTECTED ATTRIBUTES AND METHODS -> Not  used in python 
class Factory:
    _a = "pune"

    def show(self):
        print("hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super()._a)

obj = Bhopal()
obj.show2()


#3.PRIVATE ATTRIBUTES AND METHODS
"""class Factory:  # It will not get printed bcz can not be accessed outside the class
    __a = "pune"

    def __show(self):
        print("Hello i am a pune factory")

obj = Factory()

obj.__show()"""

class Factory:  # It will get printed bcz it is accessed inside  the class
    __a = "pune"

    def show(self):
        print(Factory.__a)

obj = Factory()

obj.show()

