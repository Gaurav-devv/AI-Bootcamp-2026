class Animal:
    name = "lion" #class attribute

    def __init__(self,age):
        self.age = age #instance attribute

    def show(self): #instance method
        print("How are you")

    @classmethod
    def hello(cls):
        print("how are you brother")


    @staticmethod
    def static():
        print("how are you")


obj = Animal(12)

obj.static()

