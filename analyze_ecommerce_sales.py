
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ecommerce_sales_data.csv", encoding="ISO-8859-1")

# Rename and create necessary columns
df = df.rename(columns={
    'InvoiceDate': 'order_date',
    'Description': 'product',
    'Country': 'region',
    'Quantity': 'quantity'
})

df['sales'] = df['quantity'] * df['UnitPrice']
df['category'] = 'General Merchandise'  # default for now

df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')


# Total sales by category
category_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.values, y=category_sales.index, palette="Blues_d")
plt.title("Total Sales by Product Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# Regional sales breakdown
region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="Greens")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.close()

# Monthly sales trend
monthly_sales = df.groupby('month')['sales'].sum().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# Top-selling products
top_products = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="Oranges_r")
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# Summary report
summary = {
    "Top Category": category_sales.idxmax(),
    "Top Region": region_sales.idxmax(),
    "Best Month": monthly_sales.idxmax().strftime('%B %Y'),
    "Best-Selling Product": top_products.idxmax()
}

with open("sales_summary.txt", "w") as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

print("Analysis complete. Charts and summary report saved.")
