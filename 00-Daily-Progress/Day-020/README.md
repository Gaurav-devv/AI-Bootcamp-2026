# 📅 Day 020 — Python Comprehensions

**Date:** 28 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal

Learn Python comprehensions and understand how to create collections in a shorter, cleaner, and more readable way.

---

## 📚 Topics Covered

- List Comprehension
- Conditional List Comprehension
- Nested List Comprehension
- Dictionary Comprehension
- Set Comprehension
- Using conditions with comprehensions
- Comprehensions with loops

---

## 🧠 Key Learnings

### List Comprehension

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)
List Comprehension with Condition
even = [x for x in range(1, 11) if x % 2 == 0]
print(even)
Dictionary Comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)
Set Comprehension
squares = {x ** 2 for x in range(1, 6)}
print(squares)
```
