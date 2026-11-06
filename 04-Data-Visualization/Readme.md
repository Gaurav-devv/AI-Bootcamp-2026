# 📊 Data Visualization with Python — Complete Revision Guide

A comprehensive revision guide covering Matplotlib, Seaborn, Plotly, and practical data visualization using Python.

---

## 📌 Table of Contents

1. Introduction to Data Visualization
2. Data Visualization Libraries
3. Matplotlib
4. Types of Charts in Matplotlib
5. Customizing Matplotlib Charts
6. Subplots
7. Seaborn
8. Statistical Visualizations
9. Matrix Plots and Heatmaps
10. Regression Plots
11. Plotly
12. Cufflinks
13. IPL Capstone Project
14. Choosing the Right Chart
15. Important Python Syntax Cheat Sheet
16. Best Practices
17. Learning Outcomes
18. Next Steps

---

# 1. Introduction to Data Visualization

Data Visualization is the process of representing data in graphical form, such as charts, graphs, and plots.

It helps us understand complex datasets and identify:

- Patterns
- Trends
- Relationships
- Distributions
- Outliers
- Comparisons

### Why is Data Visualization important?

Imagine having 10,000 rows of data. Reading every row manually is difficult.

Instead, we can use charts to understand the dataset quickly.

**Example:**

- A line chart helps understand trends.
- A bar chart helps compare categories.
- A histogram helps understand distributions.
- A scatter plot helps identify relationships between variables.

---

# 2. Python Libraries for Data Visualization

| Library | Purpose |
|---|---|
| Matplotlib | Creating customizable static visualizations |
| Seaborn | Statistical data visualization |
| Plotly | Interactive visualizations |
| Cufflinks | Integrates Pandas plotting with Plotly |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |

### Installation

```bash
pip install matplotlib
pip install seaborn
pip install plotly
pip install cufflinks
```

### Importing Libraries

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
```

For Cufflinks:

```python
import cufflinks as cf

cf.go_offline()
```

**Note:** Cufflinks is an older integration library. Compatibility issues can occur with modern Plotly versions. Plotly Express is generally a better choice for new projects.

---

# 3. Matplotlib

Matplotlib is one of the most popular Python libraries for creating static, animated, and interactive visualizations.

Its main plotting module is `matplotlib.pyplot`.

### Basic Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.show()
```

### Important Functions

| Function | Purpose |
|---|---|
| `plt.plot()` | Line chart |
| `plt.bar()` | Vertical bar chart |
| `plt.barh()` | Horizontal bar chart |
| `plt.hist()` | Histogram |
| `plt.scatter()` | Scatter plot |
| `plt.pie()` | Pie chart |
| `plt.boxplot()` | Box plot |
| `plt.xlabel()` | X-axis label |
| `plt.ylabel()` | Y-axis label |
| `plt.title()` | Chart title |
| `plt.legend()` | Display legend |
| `plt.grid()` | Display grid |
| `plt.show()` | Display chart |
| `plt.figure()` | Create a figure |
| `plt.subplot()` | Create subplot areas |

---

# 4. Types of Charts in Matplotlib

## 4.1 Line Chart

Used to show trends or changes across ordered observations.

```python
plt.plot(x, y)

plt.title("Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
```

## 4.2 Bar Chart

Used to compare different categories.

```python
categories = ['A', 'B', 'C', 'D']
values = [20, 40, 30, 50]

plt.bar(categories, values)

plt.title("Bar Chart")
plt.show()
```

Horizontal bar chart:

```python
plt.barh(categories, values)
plt.show()
```

## 4.3 Histogram

Used to understand the distribution of numerical data.

```python
data = [10, 20, 20, 30, 30, 30, 40, 50]

plt.hist(data, bins=5)

plt.title("Histogram")
plt.show()
```

**Important:** `bins` controls how many intervals are used to group numerical values.

## 4.4 Scatter Plot

Used to understand relationships between two numerical variables.

```python
plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

## 4.5 Pie Chart

Used to represent proportions of a whole.

```python
labels = ['Python', 'Java', 'C++']
values = [50, 30, 20]

plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%'
)

plt.title("Programming Language Share")
plt.show()
```

## 4.6 Box Plot

Used to understand the distribution, median, quartiles, and potential outliers of numerical data.

```python
data = [10, 20, 30, 40, 50, 60, 100]

plt.boxplot(data)

plt.title("Box Plot")
plt.show()
```

---

# 5. Customizing Matplotlib Charts

Matplotlib allows us to customize charts to make them easier to understand.

### Adding Colors and Markers

```python
plt.plot(
    x,
    y,
    color='red',
    marker='o',
    linestyle='--',
    linewidth=2,
    markersize=8
)

plt.show()
```

### Adding Labels and Title

```python
plt.plot(x, y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("My First Visualization")

plt.show()
```

### Adding Grid

```python
plt.plot(x, y)

plt.grid(True)

plt.show()
```

### Adding Legend

```python
plt.plot(x, y, label='Sales')

plt.legend()

plt.show()
```

### Figure Size

```python
plt.figure(figsize=(10, 5))

plt.plot(x, y)

plt.show()
```

### Saving a Figure

```python
plt.plot(x, y)

plt.savefig("my_plot.png")

plt.show()
```

**Important:** Call `savefig()` before `show()` for reliable saving across plotting environments.

---

# 6. Subplots in Matplotlib

Subplots allow us to display multiple charts in a single figure.

### Example

```python
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].plot(x, y)
ax[0, 0].set_title("Line Plot")

ax[0, 1].bar(x, y)
ax[0, 1].set_title("Bar Plot")

ax[1, 0].scatter(x, y)
ax[1, 0].set_title("Scatter Plot")

ax[1, 1].hist(y)
ax[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
```

### Understanding Subplot Parameters

```python
plt.subplot(rows, columns, position)
```

Example:

```python
plt.subplot(2, 2, 1)
```

It means:

- 2 rows
- 2 columns
- First position

---

# 7. Seaborn

Seaborn is a Python visualization library built on top of Matplotlib.

It makes statistical visualization easier and provides attractive default styles.

### Import

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Loading Built-in Dataset

```python
tips = sns.load_dataset('tips')

tips.head()
```

The Tips dataset contains information about restaurant bills and tips.

### Important Seaborn Functions

| Function | Purpose |
|---|---|
| `sns.scatterplot()` | Scatter plot |
| `sns.lineplot()` | Line plot |
| `sns.barplot()` | Statistical bar plot |
| `sns.countplot()` | Category counts |
| `sns.histplot()` | Histogram |
| `sns.kdeplot()` | Density plot |
| `sns.boxplot()` | Box plot |
| `sns.violinplot()` | Violin plot |
| `sns.stripplot()` | Strip plot |
| `sns.swarmplot()` | Swarm plot |
| `sns.heatmap()` | Heatmap |
| `sns.pairplot()` | Pairwise relationships |
| `sns.regplot()` | Regression plot |
| `sns.lmplot()` | Regression model visualization |

---

# 8. Statistical Visualizations in Seaborn

## 8.1 Scatter Plot

```python
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip'
)

plt.show()
```

Helps understand the relationship between total bill and tip.

## 8.2 Line Plot

```python
sns.lineplot(
    data=tips,
    x='size',
    y='total_bill'
)

plt.show()
```

## 8.3 Bar Plot

```python
sns.barplot(
    data=tips,
    x='day',
    y='tip'
)

plt.show()
```

**Important:** `sns.barplot()` generally displays an estimated statistic (mean by default), rather than simply counting rows.

## 8.4 Count Plot

Used to count the number of observations in each category.

```python
sns.countplot(
    data=tips,
    x='day'
)

plt.show()
```

## 8.5 Histogram

```python
sns.histplot(
    data=tips,
    x='total_bill',
    bins=20
)

plt.show()
```

## 8.6 KDE Plot

KDE stands for Kernel Density Estimation.

It provides a smoothed representation of the distribution of numerical data.

```python
sns.kdeplot(
    data=tips,
    x='total_bill'
)

plt.show()
```

## 8.7 Box Plot

```python
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill'
)

plt.show()
```

## 8.8 Violin Plot

Combines aspects of a box plot and a density plot.

```python
sns.violinplot(
    data=tips,
    x='day',
    y='total_bill'
)

plt.show()
```

## 8.9 Pair Plot

Used to visualize pairwise relationships between numerical columns.

```python
sns.pairplot(tips)

plt.show()
```

---

# 9. Matrix Plots and Heatmaps

Matrix plots visualize relationships between multiple numerical variables in a matrix-like format.

A heatmap represents values using colors.

### Correlation Matrix

Correlation measures the strength and direction of a relationship between numerical variables.

```python
corr = tips.select_dtypes(include='number').corr()

corr
```

### Creating a Heatmap

```python
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.show()
```

### Important Parameters

| Parameter | Purpose |
|---|---|
| `annot=True` | Display values inside cells |
| `cmap` | Select color palette |
| `linewidths` | Add separation between cells |
| `fmt` | Format displayed values |
| `cbar` | Show or hide color bar |

Example:

```python
sns.heatmap(
    corr,
    annot=True,
    cmap='viridis',
    linewidths=0.5,
    fmt='.2f'
)

plt.show()
```

### Understanding Correlation

Correlation values range from -1 to +1.

| Value | Meaning |
|---|---|
| +1 | Perfect positive correlation |
| 0 | No linear correlation |
| -1 | Perfect negative correlation |

**Remember:** Correlation does not prove causation.

---

# 10. Regression Plots

Regression plots help visualize relationships between variables and fit a regression line.

### Using `regplot()`

```python
sns.regplot(
    data=tips,
    x='total_bill',
    y='tip'
)

plt.show()
```

### Using `lmplot()`

```python
sns.lmplot(
    data=tips,
    x='total_bill',
    y='tip'
)
```

### Understanding Regression

Regression is a statistical technique used to understand or predict relationships between variables.

For example:

- X = Total Bill
- Y = Tip

A regression line helps visualize how the tip changes as the total bill changes.

### Difference Between `regplot()` and `lmplot()`

| regplot() | lmplot() |
|---|---|
| Returns a Matplotlib Axes | Returns a Seaborn FacetGrid |
| Works within an existing Matplotlib figure | Supports faceting into multiple plots |
| Useful for a simple regression plot | Useful for grouped regression visualizations |

---

# 11. Plotly

Plotly is a Python library used to create interactive visualizations.

Unlike ordinary static charts, Plotly charts support:

- Zooming
- Panning
- Hover information
- Interactive legends
- Exporting charts

### Import

```python
import plotly.express as px
```

## 11.1 Line Chart

```python
fig = px.line(
    tips,
    y='total_bill',
    title='Total Bill Distribution'
)

fig.show()
```

## 11.2 Bar Chart

```python
avg_tip = tips.groupby('day')['tip'].mean().reset_index()

fig = px.bar(
    avg_tip,
    x='day',
    y='tip',
    title='Average Tip by Day'
)

fig.show()
```

### Understanding `groupby()` and `reset_index()`

```python
tips.groupby('day')['tip'].mean()
```

This groups observations by day and calculates the average tip for each day.

```python
tips.groupby('day')['tip'].mean().reset_index()
```

`reset_index()` converts the resulting Series into a DataFrame, making it easier to use with Plotly Express.

## 11.3 Scatter Plot

```python
fig = px.scatter(
    tips,
    x='total_bill',
    y='tip',
    color='sex',
    title='Total Bill vs Tip'
)

fig.show()
```

## 11.4 Histogram

```python
fig = px.histogram(
    tips,
    x='total_bill',
    title='Total Bill Distribution'
)

fig.show()
```

## 11.5 Box Plot

```python
fig = px.box(
    tips,
    x='day',
    y='total_bill',
    title='Total Bill by Day'
)

fig.show()
```

### Important Plotly Express Functions

| Function | Purpose |
|---|---|
| `px.line()` | Line chart |
| `px.bar()` | Bar chart |
| `px.scatter()` | Scatter plot |
| `px.histogram()` | Histogram |
| `px.box()` | Box plot |
| `px.violin()` | Violin plot |
| `px.pie()` | Pie chart |
| `px.imshow()` | Heatmap / image-like matrix |

---

# 12. Cufflinks

Cufflinks connects Pandas plotting syntax with Plotly.

It allows us to create interactive charts directly from Pandas Series and DataFrames.

### Import

```python
import cufflinks as cf

cf.go_offline()
```

### Examples

Line Plot:

```python
tips['total_bill'].iplot(kind='line')
```

Bar Plot:

```python
tips.groupby('day')['tip'].mean().iplot(kind='bar')
```

Histogram:

```python
tips['total_bill'].iplot(kind='hist')
```

Scatter Plot:

```python
tips.iplot(
    kind='scatter',
    x='total_bill',
    y='tip',
    mode='markers'
)
```

### Important Note

Cufflinks may produce compatibility errors with newer Plotly versions.

For new projects, prefer Plotly Express.

Example equivalent:

```python
avg_tip = tips.groupby('day')['tip'].mean().reset_index()

fig = px.bar(
    avg_tip,
    x='day',
    y='tip'
)

fig.show()
```

---

# 13. IPL Capstone Project

**Project:** IPL Data Visualization Capstone Project

The purpose of this project is to apply data analysis and visualization concepts to an IPL dataset.

### Project Files

```text
04-Data-Visualization/
│
├── 01-Matplotlib.ipynb
├── 02-Seaborn.ipynb
├── 03-Matrixplot.ipynb
├── 04-Regressionplot.ipynb
├── 05-PlotlyandCufflinks.ipynb
├── 06-IPL_Capstone_Project.ipynb
│
├── basicplot.png
├── image.jpg
├── IPL.csv
│
└── Projects/
```

### Suggested Project Workflow

**Step 1: Load the Dataset**

```python
import pandas as pd

ipl = pd.read_csv('IPL.csv')

ipl.head()
```

**Step 2: Understand the Dataset**

```python
ipl.shape
ipl.info()
ipl.describe()
ipl.isnull().sum()
ipl.duplicated().sum()
```

**Step 3: Clean the Dataset**

- Identify missing values.
- Check duplicate records.
- Correct data types if necessary.
- Handle invalid or inconsistent values.

**Step 4: Perform Exploratory Data Analysis**

Explore questions such as:

- Which teams have the most wins?
- Which players have scored the most runs?
- Which bowlers have taken the most wickets?
- How do match outcomes vary across seasons?
- Which venues have hosted the most matches?

Use these questions only when the corresponding columns and information are available in your dataset.

**Step 5: Create Visualizations**

Possible visualizations:

- Bar chart for team comparisons.
- Line chart for season-wise trends.
- Histogram for score distributions.
- Heatmap for numerical correlations.
- Pie chart for selected proportions.
- Interactive Plotly charts for exploration.

**Step 6: Extract Insights**

Every visualization should answer a question.

Do not create charts just for decoration. Explain what the chart tells you.

---

# 14. Choosing the Right Chart

| Objective | Recommended Chart |
|---|---|
| Compare categories | Bar Chart |
| Show trends over time | Line Chart |
| Understand numerical distribution | Histogram |
| Find relationships between variables | Scatter Plot |
| Identify outliers | Box Plot |
| Understand data density | KDE Plot |
| Show proportions | Pie Chart |
| Compare multiple numerical variables | Heatmap |
| Understand regression relationship | Regression Plot |
| Explore data interactively | Plotly Chart |

---

# 15. Important Python Syntax Cheat Sheet

### Matplotlib

```python
plt.plot(x, y)
plt.bar(x, y)
plt.barh(x, y)
plt.hist(data)
plt.scatter(x, y)
plt.pie(values, labels=labels)
plt.boxplot(data)

plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.grid(True)
plt.show()
```

### Seaborn

```python
sns.scatterplot(data=df, x='x', y='y')
sns.lineplot(data=df, x='x', y='y')
sns.barplot(data=df, x='x', y='y')
sns.countplot(data=df, x='category')
sns.histplot(data=df, x='column')
sns.kdeplot(data=df, x='column')
sns.boxplot(data=df, x='category', y='value')
sns.violinplot(data=df, x='category', y='value')
sns.heatmap(df.corr(numeric_only=True), annot=True)
sns.pairplot(df)
sns.regplot(data=df, x='x', y='y')
```

### Plotly Express

```python
px.line(df, x='x', y='y')
px.bar(df, x='category', y='value')
px.scatter(df, x='x', y='y')
px.histogram(df, x='column')
px.box(df, x='category', y='value')
px.violin(df, x='category', y='value')
px.pie(df, names='category', values='value')
```

---

# 16. Data Visualization Best Practices

1. Always understand your dataset before plotting.
2. Choose the correct chart for your analytical question.
3. Give every chart a meaningful title.
4. Label X-axis and Y-axis clearly.
5. Avoid unnecessary colors and decorations.
6. Handle missing values before analysis.
7. Use appropriate scales.
8. Avoid misleading visualizations.
9. Use interactive charts when they add value.
10. Always write down the insights obtained from your visualizations.

---

# 17. Learning Outcomes

After completing this module, I have learned:

- Fundamentals of Data Visualization.
- Creating charts using Matplotlib.
- Statistical visualization using Seaborn.
- Working with histograms, scatter plots, box plots, and bar charts.
- Understanding heatmaps and correlation matrices.
- Visualizing regression relationships.
- Creating interactive visualizations using Plotly.
- Understanding Cufflinks and its integration with Pandas.
- Applying visualization techniques to a practical IPL dataset.

---

# 18. Next Steps

My next learning goals:

- Complete the IPL Capstone Project.
- Practice Exploratory Data Analysis (EDA).
- Improve data cleaning and analytical skills.
- Learn how to communicate insights through visualizations.
- Move towards Machine Learning using Scikit-learn.

---

## Final Revision Checklist

- [ ] Matplotlib fundamentals
- [ ] Line, bar, histogram, scatter, pie, and box plots
- [ ] Chart customization
- [ ] Subplots
- [ ] Seaborn fundamentals
- [ ] Statistical plots
- [ ] Matrix plots and heatmaps
- [ ] Regression plots
- [ ] Plotly Express
- [ ] Cufflinks basics
- [ ] IPL Capstone Project
- [ ] Exploratory Data Analysis

---

**Data Visualization — Revision Notes**

*"Data tells a story. Visualization helps us understand it."* 📊