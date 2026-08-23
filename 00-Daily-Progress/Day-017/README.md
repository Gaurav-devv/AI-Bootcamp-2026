# 📅 Day 017 — OOP: Dunder Methods & OOP Completion

**Date:** 23 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal

Complete the core Python OOP concepts and learn how **Dunder Methods** allow Python objects to work with built-in operations.

---

## 📚 Topics Covered

### Dunder Methods

- What are Dunder Methods?
- Double underscore methods
- `__init__()`
- `__str__()`
- `__len__()`
- `__add__()`
- `__eq__()`
- Special methods and Python operations
- Basic operator overloading

### OOP Concepts Completed

- Classes & Objects
- Methods
- Constructors
- Attributes
- Instance Attributes
- Class Attributes
- Instance Methods
- Class Methods
- Static Methods
- Inheritance
- Types of Inheritance
- Polymorphism
- Abstraction
- Dunder Methods

---

## 🧠 Key Learnings

- Dunder means **Double UNDERscore**.
- Dunder methods are special methods surrounded by double underscores.
- Python automatically calls certain dunder methods for built-in operations.
- `__init__()` initializes an object.
- `__str__()` controls the string representation of an object.
- `__len__()` allows an object to work with `len()`.
- `__add__()` can define how objects behave with `+`.
- Dunder methods allow us to customize the behavior of our own objects.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Gaurav")

print(student)