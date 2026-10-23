# Day 25 — Pandas Completed 🐼

**📅 Date:** 23 October 2026
**🎯 Goal:** Complete Pandas fundamentals and build a strong foundation for data analysis.

---

## 📌 Overview

On Day 25, I completed my learning of **Pandas**, a powerful Python library used for data manipulation, data cleaning, and data analysis.

Pandas helps transform raw datasets into structured, meaningful information. It works especially well with NumPy and is widely used in data science, machine learning, and AI engineering.

This milestone completes my initial learning of Pandas fundamentals and prepares me to move toward data visualization and practical data analysis projects.

## 📚 Topics Covered

### 1. Introduction to Pandas

- Understanding Pandas and its applications.
- Installing and importing Pandas.
- Understanding the relationship between Pandas and NumPy.

### 2. Pandas Data Structures

- `Series`
- `DataFrame`
- Creating Series and DataFrames.
- Understanding rows, columns, indexes, and data types.

### 3. Loading and Inspecting Data

- Reading CSV files using `pd.read_csv()`.
- Reading Excel files using `pd.read_excel()`.
- Inspecting datasets with:
  - `head()`
  - `tail()`
  - `shape`
  - `columns`
  - `index`
  - `info()`
  - `describe()`
  - `dtypes`

### 4. Selecting and Filtering Data

- Selecting individual columns and multiple columns.
- Accessing rows and columns with `loc[]` and `iloc[]`.
- Filtering rows using conditions.
- Combining conditions using `&` and `|`.
- Selecting specific rows based on column values.

### 5. Data Cleaning

- Identifying missing values with `isnull()` and `isna()`.
- Counting missing values.
- Removing missing values using `dropna()`.
- Filling missing values using `fillna()`.
- Identifying and removing duplicate records.
- Renaming columns.
- Changing data types.

### 6. Data Manipulation

- Creating and modifying columns.
- Removing rows and columns using `drop()`.
- Sorting data with `sort_values()`.
- Sorting indexes.
- Using `value_counts()`.
- Using `unique()` and `nunique()`.
- Applying conditional logic to data.

### 7. Functions and Operations

- Using built-in Pandas functions.
- Creating custom Python functions for data processing.
- Applying functions with `apply()`.
- Working with lambda functions.
- Performing operations across Series and DataFrames.

### 8. String Operations

- Using the `.str` accessor.
- Splitting text with `.str.split()`.
- Extracting information from string columns.
- Cleaning and transforming text data.
- Handling text-based columns.

### 9. Working with Dates

- Converting columns to datetime using `pd.to_datetime()`.
- Extracting year, month, and day.
- Accessing date components using `.dt`.
- Filtering records by date ranges.

### 10. Grouping and Aggregation

- Grouping records using `groupby()`.
- Calculating aggregates using `sum()`, `mean()`, `count()`, `min()`, and `max()`.
- Understanding how to summarize data by category.

### 11. Combining and Reshaping Data

- Combining DataFrames using `concat()`.
- Joining datasets using `merge()`.
- Understanding basic data reshaping concepts.

### 12. Practical Dataset Exploration

- Practicing on an anime dataset.
- Exploring columns and data types.
- Filtering records based on conditions.
- Extracting information from titles and dates.
- Applying custom functions to dataset columns.
- Using Pandas operations to answer data-related questions.

## 💻 Example: Analyzing a Dataset

```python
import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# Inspect the dataset
print(df.head())
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Filter records
filtered_df = df[df["rating"] > 8]

# Sort by rating
filtered_df = filtered_df.sort_values(
    by="rating",
    ascending=False
)

# Group and summarize
summary = df.groupby("category")["rating"].mean()

print(filtered_df)
print(summary)
```

_Note: This is a demonstration example. The column names must match those in your actual dataset._

## 🧠 Key Learnings

- Pandas makes structured data easier to analyze and manipulate.
- A DataFrame organizes information into rows and columns.
- Data cleaning is an essential step before analysis or machine learning.
- Boolean filtering helps retrieve records that meet specific conditions.
- `groupby()` and aggregation functions help summarize large datasets.
- String and datetime operations help extract useful information from unstructured-looking columns.
- Combining Pandas with NumPy and Python makes data processing more efficient.

## 🛠️ Technologies and Tools

- **Language:** Python
- **Libraries:** Pandas, NumPy
- **Environment:** Jupyter Notebook
- **Version Control:** Git and GitHub

## ✅ Day 25 Achievement

- [x] Completed the initial learning of Pandas.
- [x] Practiced data inspection and selection.
- [x] Learned data filtering and manipulation.
- [x] Explored data cleaning techniques.
- [x] Practiced string and date operations.
- [x] Worked with a real-world-style anime dataset.
- [x] Established a foundation for data analysis.

## 🚀 What's Next?

With Python, NumPy, and Pandas fundamentals covered, the next step is **Matplotlib and data visualization**.

Planned learning path:

1. Learn Matplotlib fundamentals.
2. Create charts and visualizations from datasets.
3. Complete an exploratory data analysis (EDA) project using NumPy, Pandas, and Matplotlib.
4. Begin machine learning fundamentals with Scikit-learn.
5. Continue learning Generative AI alongside the data science journey.

## 📈 Learning Journey

| Day    | Date            | Milestone                                |
| ------ | --------------- | ---------------------------------------- |
| Day 24 | 17 October 2026 | Pandas — approximately halfway completed |
| Day 25 | 23 October 2026 | Pandas — initial learning completed      |

---

**Consistency over perfection. Every day of learning builds a stronger foundation for becoming an AI Engineer.** 🚀
