import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# Load dataset
df = pd.read_csv(r'C:/Users/Abraham/Desktop/DOINGS/retail_sales_dataset.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# duplicate
df.duplicated().sum()

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Calculate mode for each column
print("\nMode Values:")
print(df.mode().iloc[0])

# Check for outliers using summary statistics (only numeric columns)
numeric_df = df.select_dtypes(include=['number'])
print("\nPotential Outliers (based on IQR method):")
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum()
print(outliers)


# Set Date as index for time-based analysis
df.set_index('Date', inplace=True)

# Top 10 Best-Selling Products
if 'Product Category' in df.columns and 'Total Amount' in df.columns:
    top_products = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_products.values, y=top_products.index)  # Removed 'palette'
    plt.xlabel("Total Sales")
    plt.ylabel("Product Category")
    plt.title("Top 10 Best-Selling Products")
    plt.show()

# Sales Trend Over Time
if 'Total Amount' in df.columns:
    monthly_sales = df.resample('ME')['Total Amount'].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Over Time")
    plt.legend()
    plt.grid()
    plt.show()

# Correlation Heatmap (only numeric columns)
numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Gender Distribution Pie Chart
if 'Gender' in df.columns:
    plt.figure(figsize=(6, 6))
    df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
    plt.title("Gender Distribution of Customers")
    plt.ylabel("")  
    plt.show()


