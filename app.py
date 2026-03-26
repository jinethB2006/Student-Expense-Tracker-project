import streamlit as st
from datetime import date
from auth import signup,login
from expense_manager import load_data,add_expense,save_budget,load_budget,clear_expenses

# -------- SESSION --------
if "user" not in st.session_state:
    st.session_state.user=None

# -------- LOGIN --------
if st.session_state.user is None:
    st.title("TrackMySpend")
    st.subheader("Login / Signup")

    menu=st.selectbox("Select Option",["Login","Signup"])

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    if menu=="Signup":
        if st.button("Create Account"):
            signup(username,password)
            st.success("Account created")

    if menu=="Login":
        if st.button("Login"):
            user=login(username,password)
            if user:
                st.session_state.user=user[0]
                st.success("Login successful")
            else:
                st.error("Invalid credentials")

# -------- MAIN APP --------
else:
    st.title("TrackMySpend")
    st.subheader("Student Expense Tracker")

    # -------- BUDGET --------
    st.header("Monthly Budget")

    budget=load_budget(st.session_state.user)
    
    new_budget=st.number_input("Set Budget",value=float(budget),min_value=0.0)

    if st.button("Save Budget"):
        save_budget(st.session_state.user,new_budget)
        st.success("Budget saved")

    st.write("Current Budget:",budget)

    # -------- ADD EXPENSE --------
    st.header("Add Expense")

    exp_date=st.date_input("Date",date.today())

    category=st.selectbox(
        "Category",
        ["Food","Travel","Books","Stationary","Other"]
    )

    amount=st.number_input("Amount",min_value=0)

    note=st.text_input("Note")

    if st.button("Add Expense"):
        add_expense(st.session_state.user,exp_date,category,amount,note)
        st.success("Expense added")

    # -------- VIEW --------
    df=load_data(st.session_state.user)

    st.header("All Expenses")
    st.dataframe(df)

    # -------- DELETE -------
    st.subheader("Manage Expenses")

    if st.button("Delete Expense History"):
        clear_expenses(st.session_state.user)
        st.success("All expenses deleted")

    # -------- SUMMARY --------
    total=df["amount"].sum() if not df.empty else 0

    st.header("Summary")

    st.write("Total Spent:",total)

    remaining=budget-total

    st.write("Remaining Budget:",remaining)

    # -------- LOGOUT --------
    if st.button("Logout"):
        st.session_state.user=None
        st.rerun()
