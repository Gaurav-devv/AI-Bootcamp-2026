"""SET"""


a = {1,2,3,4}

a.remove(2)

a.add(6)

print(a)



"""
s = {1, 2, 3}

s.add(4)         Adds an element to the set

s.remove(2)      Removes 2 (Raises an error if not found)

s.discard(5)     Removes 5 (No error if not found)

popped_element = s.pop()     Removes a random element

s.clear()        Removes all elements

"""


c = {1,2,3,4,5}
d = {4,5,6,7,8}

s  = c|d   # union of two sets
print(f"The union of sets c and d is : {s}")

s = c&d   # intersection of two sets
print(f"The intersection of sets c and d is : {s}")


s = d-c  
print(s)


s = d^c
print(s)
