# 🐼 Day 24 — Pandas: Halfway Milestone

📅 **Date:** 17 October 2026
📚 **Topic:** Pandas — Data Manipulation and Analysis
🎯 **Status:** Half Completed 🚀

---

## 📌 Overview

On Day 24 of my **AI-Bootcamp-2026** learning journey, I continued learning Pandas and completed approximately half of the module.

Pandas is an essential Python library for working with structured data. It helps with data manipulation, cleaning, filtering, and analysis.

This learning milestone strengthened my understanding of how to work with datasets using Python.

---

## 🧠 What I Learned

### 1. Introduction to Pandas

- Understanding Pandas and its applications.
- Importing Pandas using `import pandas as pd`.
- Understanding Series and DataFrames.
- Creating DataFrames from Python dictionaries.

### 2. Exploring Datasets

- `head()` — Display the first few rows.
- `tail()` — Display the last few rows.
- `shape` — Find the number of rows and columns.
- `columns` — Access column names.
- `dtypes` — Inspect column data types.
- `info()` — Understand DataFrame structure.
- `describe()` — Generate descriptive statistics.

### 3. Selecting Data

- Selecting individual columns.
- Selecting multiple columns.
- Understanding `loc[]` and `iloc[]`.
- Accessing specific rows and values.

### 4. Filtering Data

- Filtering rows using conditions.
- Comparison operators such as `>`, `<`, `==`, and `!=`.
- Combining conditions with `&` and `|`.
- Using Boolean indexing to select relevant records.

### 5. Creating and Modifying Columns

- Creating new DataFrame columns.
- Performing operations on existing columns.
- Applying conditions to generate new values.
- Understanding how DataFrames can be transformed.

### 6. Python Functions with Pandas

- Defining custom Python functions.
- Understanding how `apply()` works.
- Applying functions to values in a Series.
- Using string operations to extract useful information from text.

### 7. Practical Dataset Exploration

- Working with an anime dataset.
- Filtering anime based on scores and episode counts.
- Extracting information from title strings.
- Creating new columns from existing data.

---

## 💻 Code Practice

### Example 1: Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Gaurav", "Aman", "Rahul"],
    "Score": [85, 92, 78],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

print(df)
```

### Example 2: Filtering Data

```python
high_scores = df[df["Score"] > 80]

print(high_scores)
```

This returns only the rows where the score is greater than 80.

### Example 3: Creating a New Column

```python
df["Passed"] = df["Score"] >= 80

print(df)
```

This creates a Boolean column indicating whether each student passed the chosen threshold.

### Example 4: Finding the Highest Score

```python
highest_score = df["Score"].max()

print(highest_score)
```

This returns the maximum value in the `Score` column.

---

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- VS Code
- Git and GitHub

---

## 🎯 Why This Matters

Pandas is an important foundation for Data Science and Machine Learning because real-world datasets often require cleaning, transformation, and exploration before they can be used effectively.

My learning progression:

```text
Python Fundamentals       ✅
OOP and Python Projects   ✅
NumPy                     ✅
Pandas                    🔄 Half Completed
Matplotlib                ⏳ Upcoming
Data Analysis Project     ⏳ Upcoming
Machine Learning          ⏳ Future Goal
Generative AI             ⏳ Parallel Learning Track
```

---

## 📅 Next Learning Goals

I will continue Pandas and focus on the remaining topics, including:

- Handling missing values.
- Removing duplicate records.
- Sorting and aggregating data.
- Understanding `groupby()`.
- Combining DataFrames with `merge()` and `concat()`.
- Practising additional data-cleaning techniques.

After completing Pandas, I plan to learn Matplotlib and build a data analysis project using NumPy, Pandas, and data visualization.

---

## 🏁 Day 24 Completed

**Milestone:** Approximately 50% of Pandas completed.

Every concept I learn brings me one step closer to becoming an AI Engineer. My focus is not just on completing topics, but on understanding them and applying them through practical coding.

**Learn → Practise → Understand → Build → Document → Commit.** 🚀
