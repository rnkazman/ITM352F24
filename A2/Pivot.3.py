# Read in a CSV file with sales data 
# Create a pivot table, aggregating sales by region.
# Add in sub-columns showing the average sales by state, by sale type (retail or wholesale).

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")


pivot = sales_data.pivot_table(
   values="sale_price", index="customer_state", columns=["customer_type", "order_type"],
   aggfunc="mean", margins=True, margins_name="Totals",
)

pd.set_option("display.max_columns", None)

print(pivot)