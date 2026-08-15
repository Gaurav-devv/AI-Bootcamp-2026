





""" Now this is a ZeroDIvisionError and can be counted as
Exception and because of this exception the next line cannot
be executed+
? Like this there are many other exceptions just leave the three
errors we saw at start otherwise others are exceptions.<
? And the good part is we can handel them lets see how."""

a = int(input("Tell me your number:"))

try:
    print(10/a)

except ZeroDivisionError:
    print("Sorry you cannot divide by 0")

print("Ok , I have done the division")





a = int(input("give numberr:"))

try:
    print(10/a)

except Exception as err:
    print(f"Sorry there is an err as {err}")

else:
    print("good there is no exception")


finally:
    print("I will run no matter what")

print("Ok , I have done the division")




#use example
age = int(input("Tell me your age:"))


try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18 ")

    else:
        print("Welcome to the club")

except Exception as err:
    print(f"an error occured as {err}")


print("The club will start soon")




