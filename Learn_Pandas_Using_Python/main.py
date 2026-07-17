import pandas as pd

# pandas 2 main types:
#  dataframe = 2D labeled data structure (full spreadsheet or SQL table)
#  series = 1D labeled array (like a column)
df = pd.read_csv("orders.csv")
print(df)