"""QUESTION PRACTICE -> FOR LOOP"""

#Q1. Accept an integer and Print hello world n times 

n = int(input("Please tell your number"))

for i in range(n):
    print("Hello World")

#Q2.Print natural number up to n 
n = int(input("Please tell your number"))
for i in range(1,n+1):
    print(i)


#3.Reverse for loop. Print n to 1 

n = int(input("Please tell your number"))
for i in range(n,0,-1):
    print(i)


#4  Take a number as input and print its table 
n = int(input("Which table you want:- "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")




#5. Sum up to n terms 
n = int(input("Please tell your number"))

sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"Your sum is {sum}")


#6.Factorial of a number 
n = int(input("Please tell your number"))

fact = 1
for i in range(1,n+1):
    fact = fact*i
print(f"Your factorial  is {fact}")


#Q7. Print the sum of all even & odd numbers in a range separately

n = int(input("Tell your number"))
even = 0
odd = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Your even and odd sum are {even}, {odd}")


#Q8. Print all the factors of a number 
n = int(input("tell number for factor"))
for i in range(1, n+1):
    if n%i == 0:
        print(i)

#Q9. - Accept a number and check if it a perfect number or not.A number whose sum of factors is equal to the number itself Ex - 6 = 1, 2, 3 = 6
n = int(input("Check your number is perfect or not :"))
sum = 0
for i in range(1, n):
    if n%i == 0:
        sum +=i
if sum == n:
    print("Given number is perfect number")
else:
    print("Given number is not perfect number")


#Q10. Check wether the number is prime or not 

n = int(input("Check your number is prime or not :"))
count = 0
for i in range(1, n+1):
    if n%i == 0:
        count = count + 1

if count ==2:
    print('Your number is prime')
else:
    print("Your number is not prime")



#Q11. Reverse a string without using in build functions

a = 'GAURAV'
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
print(b)



#Q12.Check string is Pallindrome or not 
a = 'NAMAN'
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if b==a:
    print("Your string is Pallindrome")

else:
    print("Your string is not pallindrome")


    
#Q13. Count all letters, digits, and special symbols from a given string
 
a = "P@#yn26at^&i5ve"

char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr +=1
print(f" your digits are {dig}\nypur alphabets are {char}\nyour special characters are  {spchr}")



 
 