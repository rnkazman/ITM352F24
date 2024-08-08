# Read in a CSV file with sales data and print the first 5 rows
# Create a pivot table, aggregating sales by region.
import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")

# pivot = sales_data.pivot_table(
#   values="sale_price", index="sales_region", columns="order_type",
#   aggfunc="sum",
#)

pivot = sales_data.pivot_table(
   values="sale_price", index="sales_region", columns="order_type",
   aggfunc="sum", margins=True, margins_name="Totals",
)

pd.set_option("display.max_columns", None)

print(sales_data.head(5))
print(pivot)