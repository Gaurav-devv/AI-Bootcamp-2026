# 🔢 NumPy — Python for Numerical Computing

NumPy (Numerical Python) is a fundamental Python library used for numerical computing, data manipulation, and scientific computing.

It provides powerful data structures such as **NumPy arrays** and highly optimized mathematical operations that are much faster and more convenient than working with normal Python lists for numerical data.

---

## 🎯 Learning Objectives

The goal of this module is to understand NumPy from the fundamentals and build a strong foundation for:

- Data Science
- Machine Learning
- Deep Learning
- Data Analysis
- Artificial Intelligence

---

## 📚 Topics Covered

### 1. NumPy Introduction
- What is NumPy?
- Why NumPy?
- NumPy vs Python Lists
- Installing NumPy
- Importing NumPy

### 2. NumPy Arrays
- Creating NumPy arrays
- `np.array()`
- One-dimensional arrays
- Two-dimensional arrays
- Multi-dimensional arrays
- Array data types
- `dtype`

### 3. Array Properties
- `ndim`
- `shape`
- `size`
- `dtype`
- `itemsize`

### 4. Creating Arrays
- `np.zeros()`
- `np.ones()`
- `np.empty()`
- `np.full()`
- `np.arange()`
- `np.linspace()`
- Identity matrices

### 5. Array Indexing
- Accessing elements
- Positive indexing
- Negative indexing
- 2D array indexing
- Multi-dimensional indexing

### 6. Array Slicing
- Basic slicing
- Start, stop, step
- Row slicing
- Column slicing
- 2D slicing

### 7. Array Manipulation
- Reshaping arrays
- `reshape()`
- Flattening arrays
- `flatten()`
- `ravel()`
- Transpose
- `T`

### 8. Mathematical Operations
- Addition
- Subtraction
- Multiplication
- Division
- Power
- Modulus
- Scalar operations

### 9. NumPy Functions
- `np.sum()`
- `np.min()`
- `np.max()`
- `np.mean()`
- `np.median()`
- `np.std()`
- `np.var()`
- `np.sqrt()`
- `np.abs()`
- `np.round()`

### 10. Axis in NumPy
- Understanding `axis`
- `axis=0`
- `axis=1`
- Operations across rows
- Operations across columns

### 11. Array Comparison
- Comparison operators
- Boolean arrays
- Conditional filtering
- `np.where()`

### 12. Array Concatenation
- `np.concatenate()`
- `np.vstack()`
- `np.hstack()`
- Stacking arrays

### 13. Copying Arrays
- Assignment vs copying
- `copy()`
- View vs copy

### 14. Random Numbers
- `np.random`
- Random integers
- Random floats
- Random arrays
- Random seed
- `np.random.seed()`

### 15. Practical Applications
- Working with numerical datasets
- Statistical calculations
- Matrix operations
- Data preprocessing
- Preparing data for Machine Learning

---

## 🧠 Key Concepts

### NumPy Array

A NumPy array is a collection of elements of the same data type stored efficiently in memory.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)