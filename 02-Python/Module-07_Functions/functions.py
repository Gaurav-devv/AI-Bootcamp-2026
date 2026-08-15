"""FUNCTIONS"""
def hello():
    print("this is a hello function so i am doing hello")

hello()




def sum(a,b):
    print(f"The sum of your numbers is {a + b}")
sum(12,34)
sum(24,56)


def intro(name,age):
    print(f"Your name is {name} and your age is {age}")
intro("Gaurav",21)

# check string is palindrome or not
def pallindrome(str):
    rev = ""
    for i in range(len(str)-1, -1,-1):
        rev = rev + str[i]

    if rev == str :
        print("Pallindrome")
    else:
        print("Not pallindrome")


pallindrome("NAMAN")
pallindrome("CURSOR")


