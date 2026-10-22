import pandas as pd 

df = pd.read_csv("credit.csv")
df = df[df["Type"] == "Sale"]

print(df["Type"].value_counts())
print(df["Description"].head(30))

categories = {
    "Dining": ["starbucks", "TST*"],
    "Transport" : ["uber", "lyft", "southwest airlines"],
    "Groceries" : ["good nature", "trader joes", "h mart"],
    "Shopping" : ["target", "tjmaxx", "hollister", "ikea"]
    
}

def categorize(description):
    description = description.lower()
    for group, shops in categories.items():
        for shop in shops:
            if shop in description:
                return group
    return "Other"        

df["Category2"] = df["Description"].apply(categorize)
var = df["Category2"] == "Other"
df.loc[var, "Category2"] = df.loc[var, "Category"]
df["Category2"] = df["Category2"].fillna("Other")

print(df["Category2"].value_counts())
print(df[df["Category2"] == "Other"]["Description"].head(30))

# df["Amount"].sum()
# df["new_col"] = df["Description"].apply()