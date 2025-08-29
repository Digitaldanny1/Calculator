import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import sys

# Set seaborn style for better visualization
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Display first few rows
    print("First 5 rows of the Iris dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (handle missing values if any)
    if df.isnull().any().any():
        df = df.fillna(df.mean(numeric_only=True))  # Fill numerical missing values with mean
        print("\nMissing values filled with column means.")
    else:
        print("\nNo missing values found in the dataset.")

except FileNotFoundError:
    print("Error: Dataset file not found. Please ensure the file path is correct.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

# Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic Statistics for Numerical Columns:")
print(df.describe())

# Group by species and compute mean for each numerical column
print("\nMean of Numerical Columns by Species:")
group_means = df.groupby('species').mean()
print(group_means)

# Observations
print("\nObservations from Analysis:")
print("- The dataset contains 150 samples with 4 numerical features and 1 categorical feature (species).")
print("- No missing values were found, so no cleaning was needed.")
print(f"- Setosa has the smallest average sepal length ({group_means['sepal length (cm)']['setosa']:.2f} cm), while Virginica has the largest ({group_means['sepal length (cm)']['virginica']:.2f} cm).")
print(f"- Petal length varies significantly across species, with Virginica having the highest average ({group_means['petal length (cm)']['virginica']:.2f} cm).")

# Task 3: Data Visualization
# Visualization 1: Line chart (mean feature values per species)
plt.figure(figsize=(10, 6))
for column in df.columns[:-1]:  # Exclude species column
    plt.plot(group_means.index, group_means[column], marker='o', label=column)
plt.title('Mean Feature Values by Species')
plt.xlabel('Species')
plt.ylabel('Mean Value (cm)')
plt.legend()
plt.savefig('line_chart.png')
plt.close()

# Visualization 2: Bar chart (average petal length per species)
plt.figure(figsize=(8, 6))
sns.barplot(x=group_means.index, y=group_means['petal length (cm)'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.savefig('bar_chart.png')
plt.close()

# Visualization 3: Histogram (distribution of sepal length)
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.close()

# Visualization 4: Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', style='species', s=100)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.savefig('scatter_plot.png')
plt.close()

print("\nVisualizations saved as PNG files: line_chart.png, bar_chart.png, histogram.png, scatter_plot.png")
print("Analysis complete. Check the saved plots for visual insights.")