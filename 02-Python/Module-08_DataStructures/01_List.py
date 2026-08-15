"""LIST"""

a = [12,45,87,19,43,29, 67,38.5]

#1st way using index

for i in range(len(a)): 
    print(a[i])

#2nd way directly on values

for i in a:
    print(i)

    #Us examples of the methods you will get it what they are used for. 
    """
numbers = [5, 2, 9, 1, 5, 6]  # Initial list

numbers.append(10)  # Adds 10 to the end
numbers.insert(2, 15)  # Inserts 15 at index 2
numbers.extend([20, 25, 30])  # Adds multiple elements at the end
numbers.remove(5)  # Removes the first occurrence of 5
popped_item = numbers.pop(3)  # Removes and stores the element at index 3
index = numbers.index(6)  # Finds the index of 6
count_5 = numbers.count(5)  # Counts occurrences of 5
numbers.sort()  # Sorts the list in ascending order
numbers.reverse()  # Reverses the list
new_numbers = numbers.copy()  # Creates a copy of the list
numbers.clear()  # Removes all elements from the list
"""


#Q1 Print positive and negative elements of an List

l = [-45,67,12,-68,-69,34]
print("Positive elements are:")
for i in l:
    if i >= 0:
        print(i)
print("Negative elements are:")
for i in l:
    if i < 0:
        print(i)

#Q2. Mean of List elements?

l = [12,435,67,89,23,25,69]
sum = 0

for i in l:
    sum = sum + 1

print(sum/len(l))


#Q3.Find the greatest element and print its index too?
l = [12,56,62,9,32,8]
largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
         largest = l[i]
         index = i
print(f"Your largest number is {largest} at index {index}")


#Q4. Find the second greatest element?

l = [12,16,13,19,17]
largest = l[0]
sec_largest = l[0]
for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(sec_largest, largest)




#Q5. Check if List is sorted or not.
a = [12,13,14,15,16]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
else:
    print("Your list is sorted")