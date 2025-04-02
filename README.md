
# E-Commerce Sales Dashboard

## Overview

This project analyzes real e-commerce sales data to uncover business trends such as top-performing products, sales by region, monthly trends, and category performance. It is built using Python and is intended to demonstrate strong analytical and data visualization skills.

## Technologies Used

- **Python 3.9+**: Core scripting language
- **Pandas**: Data cleaning and aggregation
- **Matplotlib & Seaborn**: Data visualization

## How to Use

1. Download and extract a real dataset from [this Kaggle link](https://www.kaggle.com/datasets/carrie1/ecommerce-data).
2. Clean and rename it to `ecommerce_sales_data.csv`.
3. Ensure it has the following columns:
   - `order_date` (converted from `InvoiceDate`)
   - `product` (from `Description`)
   - `category` (manually assigned or default to 'General Merchandise')
   - `region` (from `Country`)
   - `sales` (calculated as `Quantity * UnitPrice`)
   - `quantity` (from `Quantity`)
4. Place the file in the project directory.
5. Run the script:

```
pip install pandas matplotlib seaborn
python analyze_ecommerce_sales.py
```

## Outputs

- Visualizations:
  - ![category_sales](https://github.com/user-attachments/assets/2cdee184-f09e-4943-bed3-81c303f3b86e)

  - ![monthly_sales_trend](https://github.com/user-attachments/assets/4d1cc0f2-0ba7-4191-9f35-528d5f6ccdda)

  - ![top_products](https://github.com/user-attachments/assets/ffe36c2c-5ec8-4ea0-b3fa-61ca8ce15e69)


## License

MIT License.
