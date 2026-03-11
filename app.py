import streamlit as st
from expense_manager import load_data,add_expense,save_budget,load_budget
from datetime import date

st.title("Student Expense Tracker")

st.header("Monthly Budget")

budget=load_budget()

new_budget=st.number_input("Set Budget",value=budget,min_value=0)

if st.button("Save Budget"):
    save_budget(new_budget)
    st.success("Budget saved")

st.write("Current Budget:",budget)

st.header("Add Expense")

exp_date=st.date_input("Date",date.today())

category=st.selectbox(
"Category",
["Food","Travel","Books","Stationary","Other"]
)

amount=st.number_input("Amount",min_value=0)

note=st.text_input("Note")

if st.button("Add Expense"):
    add_expense(exp_date,category,amount,note)
    st.success("Expense added")

df=load_data()

st.header("All Expenses")
st.dataframe(df)

total=df["Amount"].sum()

st.header("Summary")

st.write("Total Spent:",total)

remaining=budget-total

st.write("Remaining Budget:",remaining)