# 📅 Day 021 — Lambda, Map & Filter

**Date:** 29 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal

Learn how to use **lambda functions, `map()`, and `filter()`** to write concise and functional Python code.

---

## 📚 Topics Covered

- Lambda Functions
- Anonymous Functions
- `map()`
- `filter()`
- Lambda with `map()`
- Lambda with `filter()`
- Working with lists using functional programming concepts

---

## 🧠 Key Learnings

### Lambda Function

A lambda function is a small anonymous function written in a single expression.

```python
square = lambda x: x ** 2

print(square(5))



### map()

map() applies a function to every item in an iterable.
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)


### filter()

filter() selects elements from an iterable based on a condition
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers)
print(even)


#🔑 Main Difference

Lambda
  ↓
Creates a small anonymous function


map()
  ↓
Transforms every element


filter()
  ↓
Selects elements based on a condition


#Simple Example
[1, 2, 3, 4, 5]

       ↓ map()

[1, 4, 9, 16, 25]


[1, 2, 3, 4, 5]

       ↓ filter()

[2, 4]