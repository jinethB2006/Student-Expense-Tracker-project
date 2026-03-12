import pandas as pd
import os

FILE_PATH="data/expenses.csv"
BUDGET_FILE="data/budget.txt"

def load_data():
    os.makedirs("data",exist_ok=True)

    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size==0:
        df=pd.DataFrame(columns=["Date","Category","Amount","Note"])
        df.to_csv(FILE_PATH,index=False)
        return df
    return pd.read_csv(FILE_PATH)

def add_expense(date,category,amount,note):
    df=load_data()
    new_row={"Date":date,"Category":category,"Amount":amount,"Note":note}
    df.loc[len(df)]=new_row
    df.to_csv(FILE_PATH,index=False)

def total_expense():
    df=load_data()
    return df["Amount"].sum()

def save_budget(amount):
    os.makedirs("data",exist_ok=True)
    with open(BUDGET_FILE,"w") as f:
        f.write(str(amount))

def load_budget():
    os.makedirs("data",exist_ok=True)

    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE,"w") as f:
            f.write("0")
        return 0

    with open(BUDGET_FILE,"r") as f:
        return int(f.read()) 

def clear_expenses():
    df=pd.DataFrame(columns=["Date","Category","Amount","Note"])
    df.to_csv(FILE_PATH,index=False)
