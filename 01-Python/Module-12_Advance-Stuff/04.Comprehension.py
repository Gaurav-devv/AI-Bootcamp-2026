#List Comprehension list

l = []
for i in range(1,21):
    if i % 2 == 0 :
        l.append(i)

print(l)

#Above 5 lines of code can be written in 1 line
l = [i for i in range(1,21) if i % 2 == 0 ]
print(l)


#Dictionary Comprehension
l = {i : i**2 for i in range(1,10) }
print(l)