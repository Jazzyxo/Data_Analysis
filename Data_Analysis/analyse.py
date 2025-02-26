import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load dataset (modify file path as needed)
try:
    df = pd.read_csv("your_dataset.csv")  # Replace with actual dataset file
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Display the first few rows
display(df.head())

# Check dataset info
display(df.info())

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Handle missing values (Fill with mean for numerical, mode for categorical)
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numerical NaNs with mean
df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical NaNs with mode

# Task 2: Basic Data Analysis
# Compute summary statistics
display(df.describe())

# Group by a categorical column (Modify based on dataset columns)
if 'Category' in df.columns and 'Value' in df.columns:  # Replace with actual column names
    category_mean = df.groupby('Category')['Value'].mean()
    print("Mean value per category:")
    print(category_mean)

# Task 3: Data Visualization
sns.set_style("whitegrid")

# Line Chart (Modify time column accordingly)
if 'Date' in df.columns and 'Sales' in df.columns:  # Example time-series column
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Sales'].plot(title='Sales Trend Over Time', figsize=(10, 5))
    plt.ylabel('Sales')
    plt.xlabel('Date')
    plt.show()

# Bar Chart
if 'Category' in df.columns and 'Value' in df.columns:
    plt.figure(figsize=(8,5))
    sns.barplot(x=df['Category'], y=df['Value'])
    plt.title('Average Value per Category')
    plt.xticks(rotation=45)
    plt.show()

# Histogram
if 'NumericalColumn' in df.columns:  # Replace with actual column name
    plt.figure(figsize=(8,5))
    sns.histplot(df['NumericalColumn'], bins=20, kde=True)
    plt.title('Distribution of Numerical Column')
    plt.show()

# Scatter Plot
if 'Feature1' in df.columns and 'Feature2' in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df['Feature1'], y=df['Feature2'])
    plt.title('Feature1 vs Feature2')
    plt.xlabel('Feature1')
    plt.ylabel('Feature2')
    plt.show()

print("Analysis and visualization completed!")
