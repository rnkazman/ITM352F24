# Read in a CSV file with sales data and print the first 5 rows
import pandas as pd

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")

pd.set_option("display.max_columns", None)

print(sales_data.head(5))