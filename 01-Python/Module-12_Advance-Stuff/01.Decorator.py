class Animal:
    @property #decorator
    def show(self):
        print("Hello how are you")


obj = Animal()


obj.show



def decorate(func):
    def wrapper():
        print("I will print myself before the function hello")
        func()
        print("I will print after the function")
    return wrapper


@decorate
def hello():
    print("Hello i am Gaurav Tiwari")

hello()