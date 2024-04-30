import pandas as pd

df_sales = pd.DataFrame(pd.read_excel('supermarket_sales.xlsx'))

sales = df_sales[['Gender', 'Product line', 'Total']]

pt_sales = sales.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)


pt_sales.to_excel('pivot_table.xlsx', 'Report', startrow=1)
