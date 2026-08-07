"""Conditional Statements"""


#1. if Condition(Executes if the condition is True)
a = 13

if a > 10:
    print("I will do task A")



#2. if-else condition(Executes if True, another if False)


money = int(input("Please provide me the money:"))
if money == 10:
    print("I will have a choco bar ice cream")
else:
    print("I will have a mango dolly")


#3. if-elif-else conditions(Checks multiple condition in sequence.
rupees = int(input("Please provide me the money:"))
if rupees == 10:
    print("I will have a choco bar ice cream")
elif money == 20:
    print("I will have a mango dolly")
else:
    print("I will have a cone")