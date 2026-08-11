# 📅 Day 003 — Functions

**Date:** 09 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal of the Day

Today I continued my Python fundamentals journey and learned about **Functions**.

The main goal was to understand how functions help us:

- Organize code
- Reduce code repetition
- Reuse logic
- Break large problems into smaller parts
- Make programs easier to understand and maintain

---

## 📚 Module Completed

### Module 07 — Functions ✅

---

## 📖 Topics Covered

Today I learned:

- What is a function?
- Why functions are useful
- Defining functions using `def`
- Calling functions
- Parameters
- Arguments
- Multiple parameters
- Return values
- `print()` vs `return`
- Default arguments
- Keyword arguments
- Local variables
- Function scope
- Reusing functions
- Breaking problems into smaller functions

---

# 💻 What I Learned

## 1. Defining a Function

A function is a reusable block of code that performs a specific task.

```python
def greet():
    print("Hello!")

greet()
```

The `def` keyword is used to define a function.

The function runs when it is called.

---

## 2. Functions with Parameters

Parameters allow us to pass data into a function.

```python
def greet(name):
    print(f"Hello {name}")

greet("Gaurav")
```

Here:

- `name` is the parameter.
- `"Gaurav"` is the argument.

---

## 3. Multiple Parameters

A function can accept multiple parameters.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Here:

- `a` and `b` are parameters.
- `10` and `20` are arguments.

---

## 4. Return Statement

The `return` statement sends a value back from the function.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The returned value can be stored and used later.

---

## 5. `print()` vs `return`

This was one of the important concepts I learned today.

### `print()`

Displays the value on the screen.

```python
def add(a, b):
    print(a + b)
```

### `return`

Sends the value back to the caller.

```python
def add(a, b):
    return a + b
```

The returned value can be reused:

```python
result = add(10, 20)
print(result)
```

---

## 6. Default Arguments

A function parameter can have a default value.

```python
def greet(name="Gaurav"):
    print(f"Hello {name}")

greet()
```

If no argument is provided, the default value is used.

---

## 7. Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=20, name="Gaurav")
```

This allows arguments to be passed using their parameter names.

---

## 8. Function Scope

Variables created inside a function are generally local to that function.

```python
def test():
    message = "Hello"
    print(message)

test()
```

The variable `message` exists inside the function's local scope.

---

# 🧩 Practice Completed

I practiced creating functions for different types of problems.

### Practice areas included:

- Greeting a user
- Adding two numbers
- Performing mathematical operations
- Finding maximum values
- Checking even and odd numbers
- Calculating sums
- Passing parameters
- Returning values
- Using default arguments
- Using keyword arguments
- Calling functions multiple times
- Creating reusable logic

---

# 🧠 Important Learnings

## Functions Reduce Code Repetition

Instead of writing the same code multiple times, I can create a function once and reuse it.

```python
def add(a, b):
    return a + b
```

Then:

```python
print(add(10, 20))
print(add(50, 30))
print(add(100, 200))
```

---

## Functions Make Code More Organized

A large program can be divided into smaller functions.

```text
Program
   │
   ├── get_input()
   ├── calculate()
   ├── validate()
   └── display_result()
```

This makes programs easier to read, debug, and maintain.

---

## Functions Make Code Reusable

The same function can be used with different values.

```python
def square(number):
    return number * number

print(square(5))
print(square(10))
print(square(20))
```

---

# 🐛 Problems & Debugging

During today's learning, I focused on understanding and fixing common problems related to functions.

### Things I learned while debugging:

- A function must be defined before it can be called.
- Correct indentation is required inside functions.
- Parameters receive values when the function is called.
- `return` sends a value back to the caller.
- `print()` only displays a value.
- Local variables belong to their function scope.
- Arguments must match the function's expected parameters.

---

# 🧠 Problem-Solving Approach

I learned that functions can help break a large problem into smaller and manageable parts.

```text
Problem
   ↓
Understand the Problem
   ↓
Break it into Smaller Tasks
   ↓
Create Functions
   ↓
Pass Required Data
   ↓
Process the Data
   ↓
Return the Result
   ↓
Use the Result
```

This approach will become very important when working on larger projects.

---

# 📂 Repository Progress

```text
01-Python/
│
├── Module-01_Python-basics/       ✅
├── Module-02_Data-Types/           ✅
├── Module-03_Type-Conversion/      ✅
├── Module-04_Operators/            ✅
├── Module-05_Conditionals/         ✅
├── Module-06_Loops/                ✅
└── Module-07_Functions/            ✅
```

---

# 📈 Python Progress

| Module | Topic           | Status |
| ------ | --------------- | ------ |
| 01     | Python Basics   | ✅     |
| 02     | Data Types      | ✅     |
| 03     | Type Conversion | ✅     |
| 04     | Operators       | ✅     |
| 05     | Conditionals    | ✅     |
| 06     | Loops           | ✅     |
| 07     | Functions       | ✅     |
| 08     | Collections     | ⏳     |
| 09     | File Handling   | ⏳     |
| 10     | OOP             | ⏳     |

**Progress: 7 / 10 Python beginner modules completed 🚀**

---

# ⏱️ Study Time

**Approximate Study Time:** 4–5 hours

---

# 🧠 Reflection

## What Went Well?

- Completed Module 07 — Functions.
- Learned how to define and call functions.
- Practiced parameters and arguments.
- Understood return values.
- Learned the difference between `print()` and `return`.
- Practiced default arguments.
- Practiced keyword arguments.
- Learned the basics of function scope.
- Practiced breaking problems into smaller reusable functions.

## What Was Difficult?

- Understanding the difference between parameters and arguments.
- Understanding when to use `print()` and when to use `return`.
- Understanding how values move into and out of functions.
- Understanding local scope.

## What Do I Need to Improve?

- Solve more problems without looking at solutions.
- Practice creating functions from scratch.
- Practice solving problems using multiple functions.
- Improve my understanding of function scope.
- Become more comfortable with `return`.
- Improve my problem-solving ability.

---

# 🎯 Next Goal

## Module 08 — Python Collections

Next I will learn:

- Lists
- Tuples
- Sets
- Dictionaries
- Indexing
- Slicing
- Adding elements
- Removing elements
- Updating elements
- Iterating through collections
- Collection methods
- Nested collections
- Practical collection-based problems

---

# 🔥 Daily Learning Cycle

```text
Learn
  ↓
Understand
  ↓
Write Code Yourself
  ↓
Practice
  ↓
Debug
  ↓
Reflect
  ↓
Commit
  ↓
Push to GitHub
```

---

# 🏆 Day 003 Result

**Module 07 — Functions:** ✅ Completed

**Practice:** ✅ Completed

**Concept Understanding:** ✅

**GitHub Progress:** ✅ Updated

---

> "Don't just learn the syntax. Understand how and why the code works."

# 🚀 Day 003 Completed Successfully!
