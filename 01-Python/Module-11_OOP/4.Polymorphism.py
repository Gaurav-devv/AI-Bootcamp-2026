#TWO TYPES OF POLYMORPHISM


#1.METHOD OVERRIDING
class Animal:
    def show(self):
        print("hello I am Gaurav")

class Human(Animal):
    def show(self):
        print("How are you")

obj = Human()
obj.show()


#2. DUCK TYPING

class Animal:
    def show(self):
        print("hello I am showing")

class Human(Animal):
    def show(self):
        print("hello I am also showing")

obj = Animal()
obj2 = Human()
obj.show()
obj2.show()
