import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("sample_data_assignment_07.csv")
print(df)

# Line Plot
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Bar Plot
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
plt.scatter(df["Maths"], df["Python"])
plt.title("Maths vs Python")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.show()

# Heatmap
corr = df[["Maths", "Python", "Attendance"]].corr()
sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
