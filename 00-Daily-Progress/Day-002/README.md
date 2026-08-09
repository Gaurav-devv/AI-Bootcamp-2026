# 📅 Day 002 — Conditionals & Loops

**Date:** 08 August 2026  
**Bootcamp:** AI-Bootcamp-2026  
**Status:** ✅ Completed

---

## 🎯 Goal of the Day

Today I continued my Python fundamentals journey and learned how to:

- Make decisions using conditional statements
- Repeat instructions using loops
- Solve basic programming problems using conditions and iteration
- Combine conditions and loops to build simple programs
- Improve my problem-solving and logical thinking

---

# 📚 Modules Completed

## Module 05 — Conditionals ✅

### Topics Learned

- `if` statement
- `if-else` statement
- `if-elif-else`
- Nested conditions
- Comparison operators
- Logical operators
- Multiple conditions
- User input with conditions
- Decision making in programs

### Files Created

```text
01-Python/
└── Module-05_Conditionals/
    ├── conditionals.py
    └── practice.py
```

### Practice Completed

- Finding the greatest of two numbers
- Gender-based greeting
- Checking whether a number is even or odd
- Multiple condition problems
- Temperature-based conditions
- Practicing `if`, `elif`, and `else`
- Working with user input and conditions

---

## Module 06 — Loops ✅

### Topics Learned

- `for` loop
- `while` loop
- `range()`
- Loop iterations
- `break`
- `continue`
- Nested loops
- Using loops with conditions
- Repeating tasks using loops
- Solving problems using iteration

### Files Created

```text
01-Python/
└── Module-06_Loops/
    ├── 01_for-loop.py
    ├── 02_while-loops.py
    ├── for-loop-questions.py
    └── guessingGame.py
```

### Practice Completed

- Printing numbers using `for` loop
- Printing numbers using `while` loop
- Printing numbers within a range
- Printing even and odd numbers
- Calculating the sum up to `n`
- Finding factors of a number
- Practicing loop-based problems
- Combining loops with conditions

---

# 🎮 Mini Project — Number Guessing Game

Created a basic number guessing game using the concepts learned in:

- Variables
- User input
- `if-elif-else`
- `while` loop
- Comparison operators
- Loop control

### File

```text
guessingGame.py
```

This was my first small program where I combined multiple Python concepts together to create an interactive program.

---

# 🧠 Key Concepts Learned

## 1. Conditional Statements

Conditional statements allow a program to make decisions.

```python
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

---

## 2. `if-elif-else`

Used when multiple conditions need to be checked.

```python
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

---

## 3. For Loop

A `for` loop is useful when iterating through a sequence or range.

```python
for i in range(1, 11):
    print(i)
```

---

## 4. While Loop

A `while` loop continues executing as long as its condition remains true.

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

---

## 5. Range

The `range()` function generates a sequence of numbers.

```python
range(start, stop, step)
```

Example:

```python
for i in range(1, 11):
    print(i)
```

The `stop` value is excluded.

---

## 6. Break

`break` immediately terminates the loop.

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

---

## 7. Continue

`continue` skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

---

# 🐛 Problems & Debugging

During today's practice, I faced and solved several problems.

### Problem 1 — String Input

Learned that `input()` returns a string by default.

For numerical input:

```python
age = int(input("Enter your age: "))
```

---

### Problem 2 — Strings Need Quotes

Learned the difference between:

```python
gender == "M"
```

and:

```python
gender == M
```

The first one compares with a string.

The second one makes Python look for a variable named `M`.

---

### Problem 3 — Indentation

Learned that indentation is extremely important in Python.

```python
if condition:
    print("Inside condition")

print("Outside condition")
```

The indentation determines which statements belong to the conditional block.

---

### Problem 4 — Printing Inside a Loop

While calculating the sum from `1` to `n`, I initially placed the `print()` statement inside the loop.

This caused the intermediate sum to be printed on every iteration.

Correct approach:

```python
total = 0

for i in range(1, n + 1):
    total = total + i

print(total)
```

This prints only the final result.

---

# 🧩 Important Lessons

Today I learned that programming is not only about remembering syntax.

I need to understand the logic behind the program:

```text
Problem
   ↓
Understand the Logic
   ↓
Choose Condition / Loop
   ↓
Write Code
   ↓
Run the Program
   ↓
Debug Errors
   ↓
Improve the Solution
```

I also learned that making mistakes and debugging them is an important part of learning programming.

---

# ⏱️ Study Time

**Approximate study time:** 4–5 hours

---

# 🧠 Reflection

## What went well?

- Completed Module 05 — Conditionals.
- Completed Module 06 — Loops.
- Practiced both `for` and `while` loops.
- Solved multiple beginner programming problems.
- Created a number guessing game.
- Practiced debugging Python errors.
- Learned how indentation affects program execution.
- Continued maintaining my AI Engineering GitHub repository.

## What was difficult?

- Understanding the flow of loops.
- Understanding where code should be placed inside or outside a loop.
- Deciding when to use `if`, `elif`, and `else`.
- Converting problem statements into programming logic.
- Understanding how variables change during every loop iteration.

## What do I need to improve?

- Solve more problems without looking at solutions.
- Improve logical thinking.
- Practice nested loops.
- Practice writing programs from scratch.
- Understand program execution flow before running the code.
- Become more comfortable with solving problems independently.

---

# 📂 Repository Progress

```text
01-Python/
│
├── Module-01_Python-basics/       ✅
├── Module-02_Data-Types/           ✅
├── Module-03_Type-Conversion/      ✅
├── Module-04_Operators/            ✅
│
├── Module-05_Conditionals/         ✅
│   ├── conditionals.py
│   └── practice.py
│
└── Module-06_Loops/                ✅
    ├── 01_for-loop.py
    ├── 02_while-loops.py
    ├── for-loop-questions.py
    └── guessingGame.py
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
| 07     | Functions       | ⏳     |
| 08     | Collections     | ⏳     |
| 09     | File Handling   | ⏳     |
| 10     | OOP             | ⏳     |

**Progress: 6 Python modules completed. 🚀**

---

# 🎯 Next Goal

## Module 07 — Functions

Topics to learn:

- What are functions?
- Defining functions
- Calling functions
- Parameters
- Arguments
- Return values
- Default arguments
- Keyword arguments
- Scope
- Practical function problems

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

# 🏆 Day 002 Result

**Conditionals:** ✅ Completed  
**Loops:** ✅ Completed  
**Practice:** ✅ Completed  
**Mini Project:** 🎮 Number Guessing Game  
**GitHub Progress:** ✅ Updated

> "Don't just complete the course. Build the ability to solve problems."

## Day 002 completed successfully. 🚀
