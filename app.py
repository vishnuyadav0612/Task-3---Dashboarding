import pandas as pd

# Load the dataset
df = pd.read_excel("dataset.xlsx")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# ---------------- KPIs ----------------

total_sales = df["Total_Sales"].sum()
total_orders = df["Order_ID"].count()
total_customers = df["Customer_ID"].nunique()
average_sales = df["Total_Sales"].mean()
total_quantity = df["Quantity"].sum()

print("\n===== KPI SUMMARY =====")
print(f"Total Sales: {total_sales}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Average Sales: {average_sales:.2f}")
print(f"Total Quantity Sold: {total_quantity}")