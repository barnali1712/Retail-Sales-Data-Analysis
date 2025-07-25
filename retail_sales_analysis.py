
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_data.csv")

# Data overview
print("Dataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Revenue by region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
region_revenue.plot(kind="bar", title="Total Revenue by Region", figsize=(8,4), color='skyblue')
plt.ylabel("Revenue")
plt.xlabel("Region")
plt.tight_layout()
plt.show()

# Average unit price by product
sns.barplot(x="Product", y="Unit Price", data=df)
plt.title("Average Unit Price by Product")
plt.tight_layout()
plt.show()

# Daily units sold over time
daily_units = df.groupby("Date")["Units Sold"].sum()
daily_units.plot(figsize=(10,4), title="Daily Units Sold")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()
