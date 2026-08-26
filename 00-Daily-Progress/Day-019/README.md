# 📅 Day 019 — *args & **kwargs

**Date:** 26 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal

Learn how `*args` and `**kwargs` allow Python functions to accept a flexible number of arguments.

---

## 📚 Topics Covered

- `*args`
- `**kwargs`
- Variable-length arguments
- Positional arguments
- Keyword arguments
- Iterating over `args`
- Iterating over `kwargs`
- Using `*args` and `**kwargs` in functions
- Using `*args` and `**kwargs` with decorators

---

## 🧠 Key Learnings

### `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def add(*args):
    return sum(args)

print(add(10, 20, 30))