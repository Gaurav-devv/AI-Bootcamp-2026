This module covers the four fundamental Python data structures:

- List
- Tuple
- Set
- Dictionary



🔥 LIST vs TUPLE vs SET vs DICTIONARY

Feature	  List	  Tuple	    Set	       Dictionary
Syntax	   []	   ()	    {}	         {key:value}
Ordered	   ✅	 ✅	     ❌	         ✅
Mutable	   ✅	 ❌	     ✅	         ✅
Duplicates ✅	 ✅	     ❌	         Keys ❌ / Values ✅
Indexing   ✅	 ✅	     ❌	         By key
Slicing	   ✅	 ✅	     ❌	          ❌
Stores	  Values  Values  Unique values	  Key-value pairs
Main Use Collection	Fixed data	Unique data	Mapped data

---

# 1. 📋 LIST

## Definition

A List is an ordered and mutable collection that can store multiple values.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
Properties
✅ Ordered
✅ Mutable
✅ Allows duplicates
✅ Supports indexing
✅ Supports slicing
✅ Allows different data types
Common Methods
append()     # Add element at the end
insert()     # Add element at a specific position
remove()     # Remove a value
pop()        # Remove an element
clear()      # Remove all elements
sort()       # Sort the list
reverse()    # Reverse the list
index()      # Find index of an element
count()      # Count occurrences

Example:

numbers = [10, 20, 30]

numbers.append(40)
numbers.remove(20)

print(numbers)
2. 📦 TUPLE
Definition

A Tuple is an ordered and immutable collection.

numbers = (10, 20, 30, 40)
Properties
✅ Ordered
❌ Immutable
✅ Allows duplicates
✅ Supports indexing
✅ Supports slicing
✅ Allows different data types

Example:

student = ("Gaurav", 21, "CSE")
Tuple Methods

Tuples mainly have two methods:

index()     # Find the first occurrence index
count()     # Count occurrences

Example:

t = (5, 2, 9, 1, 5, 6)

print(t.index(9))
print(t.count(5))
Tuple Unpacking
student = ("Gaurav", 21, "CSE")

name, age, branch = student
Important

Tuples cannot be modified after creation.

t = (10, 20, 30)

# t[0] = 100  ❌ Error
3. 🟢 SET
Definition

A Set is a collection of unique elements.

numbers = {10, 20, 30, 40}
Properties
❌ Unordered
✅ Mutable
❌ Does not allow duplicates
❌ Does not support indexing
❌ Does not support normal slicing
✅ Elements must be hashable

Example:

numbers = {10, 20, 20, 30}

print(numbers)

# {10, 20, 30}

Duplicates are automatically removed.

Common Methods
add()       # Add an element
remove()    # Remove an element
discard()   # Remove without raising error if absent
pop()       # Remove an arbitrary element
clear()     # Remove all elements
Set Operations
Union

Combines elements from both sets.

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

Result:

{1, 2, 3, 4, 5}
Intersection

Returns common elements.

print(A & B)

Result:

{3}
Difference

Returns elements present in A but not B.

print(A - B)

Result:

{1, 2}
Symmetric Difference

Returns elements present in either set but not both.

print(A ^ B)

Result:

{1, 2, 4, 5}
4. 📖 DICTIONARY
Definition

A Dictionary stores data using key-value pairs.

student = {
    "name": "Gaurav",
    "age": 21,
    "branch": "CSE"
}
Properties
✅ Ordered (insertion order is preserved)
✅ Mutable
❌ Keys cannot be duplicated
✅ Values can be duplicated
❌ Keys must be hashable
✅ Values can have different data types
✅ Accessed using keys
Accessing Values
print(student["name"])
print(student["age"])

Output:

Gaurav
21
Adding / Updating Values
student["city"] = "Delhi"
student["age"] = 22
Common Methods
keys()       # Get all keys
values()     # Get all values
items()      # Get key-value pairs
get()        # Safely get a value
update()     # Update dictionary
pop()        # Remove a key-value pair
clear()      # Remove all elements



🔑 MUTABILITY
Mutable

Can be changed after creation:

List
Set
Dictionary

Example:

numbers = [10, 20, 30]
numbers[0] = 100
Immutable

Cannot be changed after creation:

Tuple
🔎 INDEXING
Data Structure	Indexing
List	✅
Tuple	✅
Set	❌
Dictionary	❌ Traditional indexing

List:

numbers[0]

Tuple:

numbers[0]

Dictionary:

student["name"]

Set:

# numbers[0] ❌
🧩 WHEN TO USE WHICH?
List

Use when you need:

Ordered data
Duplicate values
Frequent modifications
Index-based access

Example:

marks = [80, 75, 90, 80]
Tuple

Use when you need:

Ordered data
Data that should not change
Fixed collections

Example:

coordinates = (28.61, 77.20)
Set

Use when you need:

Unique values
Duplicate removal
Fast membership checking
Set operations

Example:

unique_numbers = {1, 2, 3, 4}
Dictionary

Use when you need:

Key-value relationships
Fast lookup using a key
Structured information

Example:

student = {
    "name": "Gaurav",
    "age": 21,
    "course": "CSE"
}
⚡ QUICK MEMORY TRICK
LIST
→ Ordered + Mutable + Duplicates

TUPLE
→ Ordered + Immutable + Duplicates

SET
→ Unique Values + Mutable + No Indexing

DICTIONARY
→ Key → Value + Mutable + Unique Keys
🧠 MOST IMPORTANT DIFFERENCES
Need indexing?
→ List / Tuple

Need unique values?
→ Set

Need key-value pairs?
→ Dictionary

Need to modify data?
→ List / Set / Dictionary

Need immutable data?
→ Tuple

Need duplicates?
→ List / Tuple

Need to remove duplicates?
→ Set

Need lookup using a key?
→ Dictionary