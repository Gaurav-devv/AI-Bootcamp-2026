class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"hello how are you and your name is {self.name}"

    def __add__(self, other):
        return f"your sum of ages are {self.age + other.age }"

obj = Animal("lion",12)
obj2 = Animal("dolphin",14)

print(obj + obj2)