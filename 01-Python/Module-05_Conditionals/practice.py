#Q1. Accept two numbers and print the greatest between them.
a = input("First Number :")
b = input("Second Number :")

if a>b:
    print("Greatest Number is :",a)
else:
    print("Greatest Number is :",b)



#Q2. Accept the gender from the user as char and print the  respective greeting message.

gender = str(input("Your Gender : M/F"))

if gender == 'M' or gender == 'm' :
    print("Good Morning Sir")
elif gender == 'F' or gender == 'f':
    print("Good Morning Mam")
else:
    print('Undefined Gender')
 

#Q3. Accept an integer and check whether it is an even number or odd.

num = int(input("Please tell your number :"))
if num%2 == 0 :
    print("Even Number")
else:
    print("Odd number")

#Q5. According to temperature print weather
t = int(input("Please tell the Temperature in Celcius:"))

if t< 0:
    print("Freezing Cold")
elif t >= 0 and t<10:
    print("Very cold")
elif t >= 10 and t<20:
    print("Cold")
elif t >= 20 and t<30:
    print("Pleasent")
elif t >= 30 and t<40:
    print("Hot")
elif t >= 40 and t<50:
    print("Very Hot")
else :
    print("Temperature is very Hot")
    
    
 