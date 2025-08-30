# Task 2: Exploratory Data Analysis (EDA)

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_dataset.csv' with the name of your file
df = pd.read_csv("your_dataset.csv")

# -----------------------------
# 1. Ask meaningful questions
# -----------------------------
# Examples:
# - What is the distribution of product prices?
# - Are there any missing values in the dataset?
# - Which products are the most/least expensive?
# - Are there outliers in the numerical data?

# -----------------------------
# 2. Explore the data structure
# -----------------------------
print("First 5 rows of the dataset:")
print(df.head())

print("\nData types and non-null counts:")
print(df.info())

print("\nStatistical summary of numerical columns:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

# -----------------------------
# 3. Identify trends, patterns and anomalies
# -----------------------------
# Distribution of prices
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title("Distribution of Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Boxplot to check for outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Price'])
plt.title("Outliers in Price Data")
plt.show()

# If dataset has categorical column like 'Category'
if 'Category' in df.columns:
    plt.figure(figsize=(10,6))
    sns.countplot(x='Category', data=df)
    plt.title("Count of Products per Category")
    plt.xticks(rotation=45)
    plt.show()

# -----------------------------
# 4. Test hypotheses & validate assumptions
# -----------------------------
# Example hypothesis: Higher prices may correspond to fewer items (less frequency).
# We can test correlation if there are multiple numerical columns.
if df.select_dtypes(include='number').shape[1] > 1:
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# -----------------------------
# 5. Detect potential data issues
# -----------------------------
# Check duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Check extreme values in price
print("\nTop 5 most expensive products:")
print(df.nlargest(5, 'Price'))

print("\nTop 5 cheapest products:")
print(df.nsmallest(5, 'Price'))
