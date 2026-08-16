"""FOR LOOP"""

# a = range(1,21,1)
# for i in a:
#     print(i)


for i in range(1,21,1):
    print(i)

for a in range(16,0,-1):
    print(a)


#Lets print a table of 5
for t in range(5,51,5):
    print(t)

#Print table through user input
n = int(input("Which table you want? :"))

for i in range(n,(n*10)+1,n):
    print(i)




    """LOOPS FOR STRING"""
a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))

for i in range(len(a)):
    print(a[i])

a = "Sheriyans is cool"
for i in a:
    print(i)

    """BREAK & CONTINUE"""

    for i in range(1,21):
        if i == 15:
            continue
        print(i)



for i in range(1,21):
        if i == 15:
            break
        else:
             print(i)



