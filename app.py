import pandas as pd 
import streamlit as st


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

def load_chase(file):
    df = pd.read_csv(file, index_col = False)
    df = df[df["Type"] == "Sale"].copy()
    df = df.rename(columns = {
        "Transaction Date" : "date",
        "Description": "description",
        "Amount" : "amount",
        "Category" : "bank_category",
    })
    df["amount"] = df["amount"] * -1
    return df[["date", "description", "amount", "bank_category"]]

st.title("Credit Card Expense Tracker")
uploaded = st.file_uploader("Upload your Chase CSV", type="csv")

if uploaded is not None:
    df = load_chase(uploaded)
    df["category"] = df["description"].apply(categorize)
    
    #chase fallback:
    var = df["category"] == "Other"
    df.loc[var, "category"] = df.loc[var, "bank_category"]
    df["category"] = df["category"].fillna("Other")
    
    st.metric("Total spent", f"${df['amount'].sum():,.2f}")
    
    totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    st.bar_chart(totals)
    
    st.dataframe(df.sort_values("category"))


