class Factory:
    a = 12 #Attribute

    def hello(self): #method
        print("how are you")

    print("Hello how are you i am getting initialized")

print(Factory().a)

Factory().hello() 