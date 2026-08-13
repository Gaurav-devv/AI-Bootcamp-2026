"""DICTIONARY"""

d = {10:100, 20:200, 30:300, 40:400}
# keys are used instead of index
print(d[40])

d[10] = 1000 #updating
print(d)

d[50] = 500
print(d) #creating


del d[30] #deleting
print(d)



#DICTIONARY TRAVERSING


a = {10:100, 20:200, 30:300, 40:400}

for i in a:
    print(a[i])


#help(dict)  -> with this we can read more about dictionary



#Q1. Write a Python script to merge two Python dictionaries?
d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 50:500, 60:600}

for i in d2:
    d1[i] = d2[i]

print(d1)





#Q2. Write a Python program to sum all the values in a dictionary
d1 = {10:100, 20:200, 30:300}
sum = 0
for i in d1:
    sum = sum + d1[i]


print(sum)



#Q3. Count the frequency of each elements in list

a = [1,1,1,1,1,2,3,2,3,2,3,3,2,6,5,7,7,7,7,]
count = 0
for i in a :
    if i == 3:
        count+= 1

print(count)


#now for same question in dictionary

a = [1,1,1,1,1,2,3,2,3,2,3,3,2,6,5,7,7,7,7,]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)



#Q4.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {10:100, 20:200, 40:300}
d2 = {40:400, 50:500, 60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)


