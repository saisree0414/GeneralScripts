#this script helpful to merge unique rows in same column based on duplicate rows in same column.
#pip install pandas openpyxl
import pandas as pd

# Read the Excel file
df = pd.read_excel('input.xlsx')

# Group by the first column and aggregate other columns
aggregated_df = df.groupby(df.columns[0]).agg(lambda x: ';'.join(x.astype(str).unique())).reset_index()

# Save the result to a new Excel file
aggregated_df.to_excel('output.xlsx', index=False)

