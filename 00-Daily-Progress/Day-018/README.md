# 📅 Day 018 — Python Decorators

**Date:** 24 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal

Learn **Decorators in Python** and understand how functions can be modified or extended without changing their original code.

---

## 📚 Topics Covered

- Functions as objects
- Higher-order functions
- Nested functions
- Passing functions as arguments
- Returning functions
- Decorators
- `@` decorator syntax
- Wrapper functions
- `*args` and `**kwargs`
- Practical use of decorators

---

## 🧠 Key Learnings

- Functions in Python can be passed as arguments and returned from other functions.
- A decorator is a function that modifies or extends the behavior of another function.
- The `@decorator` syntax is a shorter way of applying a decorator.
- A wrapper function is commonly used inside decorators.
- `*args` and `**kwargs` allow decorators to work with functions having different arguments.

### Basic Example

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def hello():
    print("Hello!")


hello()