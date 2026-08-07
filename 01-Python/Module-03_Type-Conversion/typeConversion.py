"""TYPE - CONVERSION"""
#There are 2 types of conversion and . Implicit Explicit.


a= 12
a = str(a)
print(type(a))


#1.Implicit 
"""In this python automatically

converts data from one data 

type to another."""

b = 12
print(b /2)

#2. Explicit
"""int() - Integer

 float() - Float

 complex() - Complex

 str() - String 

 list() - List

 tuple() - Tuple

 set() - Set

 dict() - Dictionary

 bool() - Boolean"""


#OUTPUT
name = "Gaurav"
age = "21"

#different ways to print something

print(name) #different ways to print something
print(age)
print(name,age)

print("hello my name is",name,"and my age is",age)
print(f"my name is {name} and my age is {age}") #formatted string use case

# INPUT

Age = int(input("Hello what is your age"))
print(Age)