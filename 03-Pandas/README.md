# 🐼 Pandas — Learning & Revision Notes

**Learning Journey:** AI-Bootcamp-2026
**Topic:** Pandas
**Status:** Completed ✅
**Purpose:** Learning documentation, quick revision, and future reference.

---

## 📌 1. What Is Pandas?

**Pandas** is a Python library used for data manipulation, cleaning, analysis, and exploration.

It makes working with structured data easier, especially data stored in tables, CSV files, and Excel files.

### Why use Pandas?

- Read and write datasets.
- Organize data into rows and columns.
- Select and filter data.
- Handle missing values.
- Remove duplicate records.
- Perform statistical calculations.
- Group and summarize data.
- Clean and transform text.
- Prepare datasets for Machine Learning.

### Import Pandas

```python
import pandas as pd
```

`pd` is the conventional alias for Pandas.

---

## 📊 2. Series vs DataFrame

Pandas has two fundamental data structures.

### Series

A Series is a one-dimensional labeled collection of values.

```python
import pandas as pd

scores = pd.Series([9.1, 8.7, 9.5])

print(scores)
```

### DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

```python
data = {
    "Name": ["Gaurav", "Aman", "Rahul"],
    "Age": [21, 22, 20],
    "Score": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

|     | Name   | Age | Score |
| --: | ------ | --: | ----: |
|   0 | Gaurav |  21 |    85 |
|   1 | Aman   |  22 |    90 |
|   2 | Rahul  |  20 |    78 |

**Remember:**

- Series → One-dimensional data.
- DataFrame → Two-dimensional tabular data.

---

## 📂 3. Reading and Writing Data

### Read a CSV file

```python
df = pd.read_csv("data.csv")
```

### Read an Excel file

```python
df = pd.read_excel("data.xlsx")
```

### Read a JSON file

```python
df = pd.read_json("data.json")
```

### Save a DataFrame to CSV

```python
df.to_csv("output.csv", index=False)
```

`index=False` prevents Pandas from writing the DataFrame index as an additional column.

### Display the first five rows

```python
df.head()
```

### Display the first ten rows

```python
df.head(10)
```

### Display the last five rows

```python
df.tail()
```

---

## 🔍 4. Understanding Your Dataset

These commands help you inspect a dataset before analyzing it.

| Command         | Purpose                                             |
| --------------- | --------------------------------------------------- |
| `df.head()`     | Display the first five rows                         |
| `df.tail()`     | Display the last five rows                          |
| `df.shape`      | Return the number of rows and columns               |
| `df.columns`    | Display column names                                |
| `df.index`      | Display index information                           |
| `df.dtypes`     | Display data types of columns                       |
| `df.info()`     | Show column names, data types, and non-null counts  |
| `df.describe()` | Generate descriptive statistics for numeric columns |
| `df.size`       | Return the total number of elements                 |
| `df.ndim`       | Return the number of dimensions                     |

Example:

```python
print(df.shape)
print(df.columns)
print(df.dtypes)

df.info()
df.describe()
```

**Important:** `shape`, `columns`, and `dtypes` are attributes, so they do not require parentheses.

---

## 🎯 5. Selecting Columns

Consider this DataFrame:

```python
df = pd.DataFrame({
    "Name": ["Gaurav", "Aman", "Rahul"],
    "Age": [21, 22, 20],
    "Score": [85, 90, 78]
})
```

### Select one column

```python
df["Name"]
```

Returns a Series.

### Select multiple columns

```python
df[["Name", "Score"]]
```

Returns a DataFrame.

### Select a value using row and column labels

```python
df.loc[0, "Name"]
```

Returns the value in the row labeled `0` and the `Name` column.

### Select using integer positions

```python
df.iloc[0, 0]
```

Returns the first row's first column value.

**Difference:**

- `loc` → Label-based selection.
- `iloc` → Integer-position-based selection.

---

## ✂️ 6. Filtering Rows

Filtering selects rows that satisfy a condition.

### Find students with scores greater than 80

```python
df[df["Score"] > 80]
```

### Find students aged 21 or older

```python
df[df["Age"] >= 21]
```

### Use multiple conditions

```python
df[(df["Age"] >= 21) & (df["Score"] > 80)]
```

### Use OR conditions

```python
df[(df["Age"] == 20) | (df["Score"] >= 90)]
```

### Exclude a condition

```python
df[~(df["Age"] == 21)]
```

**Remember:**

- `&` → AND.
- `|` → OR.
- `~` → NOT.

Put each condition inside parentheses when combining conditions.

### Filter using `isin()`

```python
df[df["Age"].isin([20, 21])]
```

This selects rows where the age is either 20 or 21.

### Filter using `between()`

```python
df[df["Score"].between(80, 90)]
```

This selects scores between 80 and 90, including both boundaries by default.

---

## ➕ 7. Creating and Modifying Columns

### Create a new column

```python
df["Passed"] = df["Score"] >= 80
```

This creates a Boolean column containing `True` or `False`.

### Create a calculated column

```python
df["Score_Doubled"] = df["Score"] * 2
```

### Rename a column

```python
df = df.rename(columns={"Score": "Marks"})
```

### Delete a column

```python
df = df.drop(columns=["Marks"])
```

### Apply a condition with `np.where()`

```python
import numpy as np

df["Result"] = np.where(df["Score"] >= 80, "Pass", "Fail")
```

`np.where()` chooses one value when a condition is true and another when it is false.

---

## 🧹 8. Handling Missing Values

Missing data can affect analysis and Machine Learning.

### Check missing values

```python
df.isnull()
```

### Count missing values in each column

```python
df.isnull().sum()
```

### Count non-missing values

```python
df.count()
```

### Remove rows containing missing values

```python
df.dropna()
```

### Fill missing values

```python
df["Score"] = df["Score"].fillna(df["Score"].mean())
```

This fills missing scores with the column's mean.

### Fill missing values with a fixed value

```python
df["Name"] = df["Name"].fillna("Unknown")
```

**Important:** `dropna()` returns a modified result by default rather than changing the original DataFrame in place. Assign the result if you want to keep the change.

---

## 🔁 9. Handling Duplicate Records

### Check for duplicates

```python
df.duplicated()
```

### Count duplicate rows

```python
df.duplicated().sum()
```

### Remove duplicate rows

```python
df = df.drop_duplicates()
```

### Check duplicates based on a particular column

```python
df.duplicated(subset=["Name"])
```

### Remove duplicates based on a particular column

```python
df = df.drop_duplicates(subset=["Name"])
```

By default, Pandas keeps the first occurrence of a duplicate.

---

## 🔃 10. Sorting Data

### Sort by score in ascending order

```python
df.sort_values(by="Score")
```

### Sort by score in descending order

```python
df.sort_values(by="Score", ascending=False)
```

### Sort by multiple columns

```python
df.sort_values(
    by=["Age", "Score"],
    ascending=[True, False]
)
```

This sorts by age in ascending order and then by score in descending order within each age.

---

## 📈 11. Statistical Operations

Pandas provides convenient methods for summarizing numerical data.

| Method                       | Purpose                         |
| ---------------------------- | ------------------------------- |
| `df["Score"].mean()`         | Calculate the mean              |
| `df["Score"].median()`       | Calculate the median            |
| `df["Score"].mode()`         | Find the mode                   |
| `df["Score"].sum()`          | Calculate the sum               |
| `df["Score"].min()`          | Find the minimum                |
| `df["Score"].max()`          | Find the maximum                |
| `df["Score"].count()`        | Count non-missing values        |
| `df["Score"].std()`          | Calculate standard deviation    |
| `df["Score"].var()`          | Calculate variance              |
| `df["Score"].nunique()`      | Count distinct values           |
| `df["Score"].value_counts()` | Count occurrences of each value |

Example:

```python
print("Average:", df["Score"].mean())
print("Highest:", df["Score"].max())
print("Lowest:", df["Score"].min())
```

These operations are useful when exploring real datasets.

---

## 📦 12. Grouping Data with `groupby()`

`groupby()` groups rows according to one or more columns so that you can calculate summaries for each group.

Example:

```python
df = pd.DataFrame({
    "Department": ["AI", "Web", "AI", "Web", "AI"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
})
```

### Average salary by department

```python
df.groupby("Department")["Salary"].mean()
```

### Total salary by department

```python
df.groupby("Department")["Salary"].sum()
```

### Multiple aggregations

```python
df.groupby("Department")["Salary"].agg(
    ["mean", "min", "max", "count"]
)
```

**Remember the pattern:**

```python
df.groupby("group_column")["numeric_column"].aggregation()
```

For example:

```python
df.groupby("Department")["Salary"].mean()
```

This groups the data by department and calculates the average salary for each department.

---

## 🧩 13. Understanding `apply()`

The `apply()` method applies a function to a Series or along an axis of a DataFrame.

### Example using a custom function

```python
def categorize_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    else:
        return "Needs Improvement"
```

Apply the function to a column:

```python
df["Category"] = df["Salary"].apply(categorize_score)
```

The example above demonstrates the mechanics of `apply()`, but using salary to categorize a score would not be meaningful. A more appropriate example would use an actual score column:

```python
scores = pd.Series([95, 85, 70])

categories = scores.apply(categorize_score)

print(categories)
```

Output:

```text
0              Excellent
1                   Good
2    Needs Improvement
dtype: object
```

### How it works

```text
Series
   |
   v
apply(function)
   |
   v
Function runs on each value
   |
   v
New Series containing results
```

Use `apply()` when a custom function is helpful. For simple arithmetic or straightforward conditions, vectorized Pandas operations are often preferable.

---

## 🔤 14. String Operations

Pandas provides the `.str` accessor for working with text throughout a Series.

### Convert text to lowercase

```python
df["Name"].str.lower()
```

### Convert text to uppercase

```python
df["Name"].str.upper()
```

### Remove surrounding whitespace

```python
df["Name"] = df["Name"].str.strip()
```

### Find strings containing a word

```python
df[df["Name"].str.contains("Gaurav", case=False, na=False)]
```

### Replace text

```python
df["Name"] = df["Name"].str.replace("Old", "New", regex=False)
```

### Split a string

```python
df["Name"].str.split()
```

### Extract text after a marker

```python
df["Date"] = df["Title"].str.split("eps)", n=1).str[1].str.strip()
```

This last example assumes the `Title` column contains the marker `eps)` before the date range.

**Remember:**

- `.str.lower()` → Lowercase text.
- `.str.contains()` → Search for text.
- `.str.replace()` → Replace text.
- `.str.split()` → Split text into pieces.
- `.str.strip()` → Remove surrounding whitespace.

---

## 🧮 15. Working with `loc` and `iloc`

These are two important ways to select rows and columns.

### Using `loc`

```python
df.loc[0, "Name"]
```

Selects a value by index label and column label.

### Select a range of index labels

```python
df.loc[0:2, ["Name", "Score"]]
```

With a standard integer index, this includes labels `0`, `1`, and `2`.

### Using `iloc`

```python
df.iloc[0, 0]
```

Selects the first row's first column by position.

### Select rows by position

```python
df.iloc[0:3, 0:2]
```

Selects the first three rows and first two columns. The ending positions are excluded.

**Key distinction:** `loc` uses labels; `iloc` uses positions.

---

## 🔗 16. Combining DataFrames

### Concatenate DataFrames vertically

```python
combined = pd.concat([df1, df2], ignore_index=True)
```

This stacks rows from both DataFrames.

### Merge DataFrames using a common key

```python
merged = pd.merge(df1, df2, on="ID", how="inner")
```

This combines matching records using the `ID` column.

### Common merge types

| Type    | Meaning                                 |
| ------- | --------------------------------------- |
| `inner` | Keep matching keys from both DataFrames |
| `left`  | Keep all keys from the left DataFrame   |
| `right` | Keep all keys from the right DataFrame  |
| `outer` | Keep all keys from both DataFrames      |

Use `merge()` when joining related datasets and `concat()` when stacking compatible datasets.

---

## 📊 17. Selecting Extreme Values

### Find the row with the maximum episode count

```python
df[df["Episodes"] == df["Episodes"].max()]
```

This works in three steps:

1. `df["Episodes"].max()` finds the maximum episode count.
2. `df["Episodes"] == ...` creates a Boolean condition.
3. `df[...]` returns rows satisfying the condition.

### Find the five rows with the largest episode counts

```python
df.nlargest(5, "Episodes")
```

### Find the five rows with the highest scores

```python
df.nlargest(5, "Score")
```

### Find the five rows with the smallest scores

```python
df.nsmallest(5, "Score")
```

These operations are especially useful for ranking and exploratory data analysis.

---

## 🎌 18. Practical Example — Anime Dataset

During Pandas practice, I worked with an anime dataset containing columns such as:

- `Rank`
- `Title`
- `Score`
- `Episodes`
- `Total Time`

This dataset helped me practise filtering, selecting rows, extracting text, and identifying records with high scores or episode counts.

### Inspect the dataset

```python
df.head()
df.shape
df.info()
df.describe()
```

### Find the anime with the highest episode count

```python
df[df["Episodes"] == df["Episodes"].max()]
```

### Find the five anime with the most episodes

```python
df.nlargest(5, "Episodes")
```

### Find the five highest-scoring anime

```python
df.nlargest(5, "Score")
```

### Create a column containing extracted date ranges

```python
df["Total Time"] = (
    df["Title"]
    .str.split("eps)", n=1)
    .str[1]
    .str.strip()
)
```

This extracts the portion after `eps)` from each title.

Before using it on a different dataset, check whether the title format is consistent and whether missing values need special handling.

### Select relevant columns

```python
df[["Rank", "Title", "Score", "Episodes"]].head()
```

### Filter high-scoring anime

```python
df[df["Score"] >= 9.0]
```

These exercises demonstrate how Pandas can turn a raw dataset into useful information.

---

## ⚡ 19. Important Pandas Patterns to Remember

### Pattern 1: Inspect

```python
df.head()
df.info()
df.describe()
```

### Pattern 2: Select

```python
df["Column"]
df[["Column1", "Column2"]]
df.loc[0, "Column"]
df.iloc[0, 0]
```

### Pattern 3: Filter

```python
df[df["Column"] > value]
```

### Pattern 4: Sort

```python
df.sort_values("Column", ascending=False)
```

### Pattern 5: Clean

```python
df.isnull().sum()
df.dropna()
df.drop_duplicates()
```

### Pattern 6: Aggregate

```python
df.groupby("Category")["Value"].mean()
```

### Pattern 7: Transform

```python
df["New Column"] = df["Old Column"].apply(function)
```

### Pattern 8: Extract text

```python
df["Column"].str.split("marker", n=1).str[1].str.strip()
```

### Pattern 9: Find extreme values

```python
df.nlargest(5, "Column")
df.nsmallest(5, "Column")
```

---

## 🚀 20. Why Pandas Matters for AI and Machine Learning

Real-world AI projects require more than building models.

Data usually needs to be inspected, cleaned, transformed, and prepared before training.

A typical workflow looks like this:

```text
Raw Dataset
     |
     v
Load with Pandas
     |
     v
Inspect the Data
     |
     v
Clean Missing Values
     |
     v
Remove Duplicates
     |
     v
Select Relevant Features
     |
     v
Analyze and Visualize
     |
     v
Prepare Data for Machine Learning
     |
     v
Train and Evaluate a Model
```

Pandas is useful for:

- Data cleaning.
- Exploratory data analysis.
- Feature preparation.
- Dataset inspection.
- Combining datasets.
- Preparing structured data for Machine Learning.

---

## 📚 21. Pandas Revision Checklist

Use this checklist to assess your understanding.

- [x] Import Pandas
- [x] Understand Series and DataFrames
- [x] Read datasets
- [x] Inspect rows, columns, and data types
- [x] Select columns
- [x] Filter rows
- [x] Use `loc` and `iloc`
- [x] Create and modify columns
- [x] Understand missing values
- [x] Remove duplicates
- [x] Sort data
- [x] Calculate statistics
- [x] Group and aggregate data
- [x] Understand `apply()`
- [x] Perform string operations
- [x] Understand `concat()` and `merge()`
- [x] Find maximum values and top records
- [x] Practise on an anime dataset

**Note:** These checkboxes document my learning milestones. I should periodically test myself without referring to these notes to verify that I can reproduce the techniques independently.

---

## 🎯 22. What Comes Next?

My next learning milestones are:

1. **Matplotlib** — Learn to visualize data.
2. **Data Analysis Project** — Combine Pandas, NumPy, and Matplotlib.
3. **Machine Learning** — Learn fundamental algorithms and model evaluation.
4. **Deep Learning** — Study neural networks and PyTorch.
5. **Generative AI** — Learn LLMs, embeddings, RAG, tool calling, and agents.

I will also continue my Generative AI learning track alongside my Python and data-analysis studies.

---

## 🏁 Pandas Completed

Pandas has helped me move from writing Python programs to manipulating and analyzing structured datasets.

My next goal is to use these skills to discover patterns in real data and communicate those findings through visualizations.

**Learning principle:** Understand the problem, write the code yourself, inspect the result, and explain why the solution works.
