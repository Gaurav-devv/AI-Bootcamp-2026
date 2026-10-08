# 🔢 Day 23 — NumPy Completed

📅 **Date:** 8 September 2026  
📚 **Topic:** NumPy  
🎯 **Status:** Completed ✅

---

## 📌 Overview

Today I completed the **NumPy** module as part of my AI-Bootcamp-2026 journey.

NumPy (Numerical Python) is one of the most important Python libraries for numerical computing and forms a strong foundation for **Data Science, Machine Learning, Deep Learning, and AI**.

---

## 🧠 What I Learned

During this module, I learned how to work with NumPy arrays and perform efficient numerical operations.

### 🔹 NumPy Basics

- What is NumPy?
- Why NumPy is used
- Installing and importing NumPy
- NumPy version
- NumPy arrays

### 🔹 Arrays

- Creating NumPy arrays
- 1D arrays
- 2D arrays
- Multi-dimensional arrays
- Array data types

### 🔹 Array Properties

- `ndim`
- `shape`
- `size`
- `dtype`
- `itemsize`

### 🔹 Array Creation

- `np.array()`
- `np.zeros()`
- `np.ones()`
- `np.full()`
- `np.arange()`
- `np.linspace()`

### 🔹 Indexing & Slicing

- Positive indexing
- Negative indexing
- 2D indexing
- Array slicing
- Row and column selection

### 🔹 Array Manipulation

- `reshape()`
- `flatten()`
- `ravel()`
- Transpose
- `T`

### 🔹 Mathematical Operations

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Modulus
- Scalar operations

### 🔹 Statistical Operations

- `np.sum()`
- `np.min()`
- `np.max()`
- `np.mean()`
- `np.median()`
- `np.std()`
- `np.var()`

### 🔹 Axis

- Understanding `axis`
- `axis=0`
- `axis=1`
- Row-wise operations
- Column-wise operations

### 🔹 Filtering

- Comparison operators
- Boolean arrays
- Conditional filtering
- `np.where()`

### 🔹 Combining Arrays

- `np.concatenate()`
- `np.vstack()`
- `np.hstack()`

### 🔹 Copy & View

- Difference between copy and view
- `copy()`
- Understanding shared data

### 🔹 Random Numbers

- `np.random`
- Random integers
- Random floats
- Random arrays
- Random seed

---

## 💻 Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(numbers.shape)
print(numbers.mean())
print(numbers.max())