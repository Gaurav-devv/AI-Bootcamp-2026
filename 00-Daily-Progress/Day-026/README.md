# Day 26 — Matplotlib Completed 📊

**📅 Date:** 28 October 2026
**🎯 Goal:** Complete Matplotlib fundamentals and learn to visualize data using Python.

---

## 📌 Overview

On Day 26, I completed my learning of **Matplotlib**, a popular Python library for data visualization.

Matplotlib helps transform raw data into meaningful visual representations. It allows us to identify patterns, compare values, understand distributions, and communicate insights through charts and graphs.

After completing Python fundamentals, NumPy, and Pandas, learning Matplotlib was another important milestone in my journey toward becoming an AI Engineer.

## 📚 Topics Covered

### 1. Introduction to Matplotlib

- Understanding data visualization.
- Introduction to `matplotlib.pyplot`.
- Creating and displaying plots.

### 2. Line Plots

- Creating line charts using `plt.plot()`.
- Visualizing trends and changes.
- Customizing lines and markers.

### 3. Bar Charts

- Creating vertical bar charts using `plt.bar()`.
- Creating horizontal bar charts using `plt.barh()`.
- Comparing values across categories.

### 4. Scatter Plots

- Creating scatter plots using `plt.scatter()`.
- Exploring relationships between numerical variables.
- Identifying patterns in data.

### 5. Histograms

- Creating histograms using `plt.hist()`.
- Understanding numerical data distributions.
- Exploring the frequency of values.

### 6. Plot Customization

- Adding titles using `plt.title()`.
- Labeling axes using `plt.xlabel()` and `plt.ylabel()`.
- Adding legends using `plt.legend()`.
- Displaying grid lines using `plt.grid()`.
- Customizing markers, colors, and line styles.

### 7. Subplots

- Understanding multiple plots in one figure.
- Creating subplots using `plt.subplot()` and `plt.subplots()`.
- Comparing different visualizations.

### 8. Figures and Axes

- Understanding figures and axes.
- Creating figures and managing individual plots.
- Using the object-oriented plotting interface.

### 9. Visualizing Data with NumPy and Pandas

- Plotting NumPy arrays.
- Visualizing Pandas Series and DataFrame columns.
- Selecting dataset columns for visualization.
- Exploring data through graphical representations.

## 💻 Practical Examples

### Line Plot

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
productivity = [2, 4, 3, 6, 8]

plt.plot(days, productivity, marker="o", label="Productivity")

plt.title("Daily Productivity")
plt.xlabel("Day")
plt.ylabel("Productivity Score")
plt.legend()
plt.grid(True)

plt.show()
```

### Bar Chart

```python
import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "Matplotlib"]
hours = [20, 12, 18, 10]

plt.bar(subjects, hours)

plt.title("Learning Progress")
plt.xlabel("Subjects")
plt.ylabel("Hours Studied")

plt.show()
```

### Scatter Plot

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
scores = [40, 45, 55, 65, 75, 85]

plt.scatter(study_hours, scores)

plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")

plt.show()
```

### Histogram

```python
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
```

## 🧠 Key Learnings

- Data visualization makes data easier to understand.
- Line plots help identify trends.
- Bar charts help compare categories.
- Scatter plots help explore relationships between numerical variables.
- Histograms help understand data distributions.
- Titles, labels, legends, and grids make charts more informative.
- NumPy and Pandas can be combined with Matplotlib for effective data analysis.

## 🛠️ Technologies and Tools

- **Language:** Python
- **Libraries:** Matplotlib, NumPy, Pandas
- **Environment:** Jupyter Notebook
- **Version Control:** Git and GitHub

## ✅ Day 26 Achievements

- [x] Completed Matplotlib fundamentals.
- [x] Practiced different types of charts.
- [x] Learned plot customization.
- [x] Explored figures and axes.
- [x] Practiced data visualization.
- [x] Connected Matplotlib with NumPy and Pandas.

## 🚀 What's Next?

With Python, NumPy, Pandas, and Matplotlib fundamentals completed, the next step is to apply these skills in a practical **Exploratory Data Analysis (EDA) project**.

### Planned Learning Path

1. Select a real-world dataset.
2. Load and inspect the data using Pandas.
3. Clean missing values and duplicate records.
4. Perform exploratory data analysis.
5. Create visualizations using Matplotlib.
6. Identify patterns, trends, and useful insights.
7. Document the project and publish it on GitHub.

After completing an EDA project, I plan to move toward **Machine Learning with Scikit-learn** while continuing to develop my Generative AI skills.

## 📈 Learning Journey

| Day    | Date            | Milestone                                |
| ------ | --------------- | ---------------------------------------- |
| Day 24 | 17 October 2026 | Pandas — approximately halfway completed |
| Day 25 | 23 October 2026 | Pandas — initial learning completed      |
| Day 26 | 28 October 2026 | Matplotlib — fundamentals completed      |

---

**Learning by building. Turning data into insights, one visualization at a time.** 🚀
