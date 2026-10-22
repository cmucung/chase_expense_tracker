import pandas as pd 

df = pd.read_csv("credit.csv")
index_col = False

print(df.head())
print(df.columns)
print(df["Amount"])
# df["Amount"].sum()
# df["new_col"] = df["Description"].apply()