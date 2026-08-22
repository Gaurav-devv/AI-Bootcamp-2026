class Factorymumbai: #parent class / superclass
    a = "I am an attribute mentioned inside Factory"
    def hello(self):
        print("hello i am a method mentioned inside Factory")

class Factorypune(Factorymumbai): #Child class
    pass

obj  = Factorymumbai()

print(obj.a)

obj2 = Factorypune()
print(obj2.hello())


#

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")


class Human(Animal):
    pass

animal1 = Animal("Lion")
person1 = Human("gaurav")

person1.show()
animal1.show()


#SINGLE INHERITANCE

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")


class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
            print(f"hello your name is {self.name},{self.age}")


animal1 = Animal("Lion")
person1 = Human("gaurav",21)

person1.show()
animal1.show()


#MULTIPLE INHERITANCE
class Animal:
    def __init__(self,name):
        self.name = name
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Robots(Human,Animal):
    name3 = "charli123"

obj = Robots("Gaurav",21)

print(obj.name)
print(obj.age)
print(obj.name)


#MUTILEVEL INHERITANCE
class Factory:
    def __init__(self, material,zips,):
        self.material = material
        self.zips = zips
        
class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color, )
        self.pockets = pockets


obj = PuneFactory()
