import streamlit as st
import pandas as pd
import joblib

model1=joblib.load("random_forest_model_joblib")
st.title("Bank Marketing Prediction")
st.write("Predict whether a customer will subscribe to a bank term deposit.")


st.header("Customer Information")

age = st.number_input("Age", min_value=18, max_value=100, value=30)


job = st.selectbox("Job", [
    "admin.", "blue-collar", "entrepreneur",
    "housemaid", "management", "retired",
    "self-employed", "services", "student",
    "technician", "unemployed", "unknown"
])



marital = st.selectbox("Marital Status", [
    "single", "married", "divorced", "unknown"
])


education = st.selectbox("Education", [
    "university.degree", "high.school",
    "basic.9y", "basic.6y", "basic.4y",
    "professional.course", "illiterate", "unknown"
])

default = st.selectbox("Credit Default", [
    "no", "yes", "unknown"
])

housing = st.selectbox("Housing Loan", [
    "no", "yes", "unknown"
])

loan = st.selectbox("Personal Loan", [
    "no", "yes", "unknown"
])

contact = st.selectbox("Contact Type", [
    "cellular", "telephone"
])

st.header("Campaign Information")


month = st.selectbox("Month", [
    "mar", "apr", "may", "jun", "jul",
    "aug", "sep", "oct", "nov", "dec"
])


day_of_week = st.selectbox("Day of Week", [
    "mon", "tue", "wed", "thu", "fri"
])

campaign = st.number_input(
    "Number of Contacts",
    min_value=1,
    value=1
)

pdays = st.number_input(
    "Days Since Previous Contact",
    min_value=0,
    value=999
)

previous = st.number_input(
    "Previous Contacts",
    min_value=0,
    value=0
)

poutcome = st.selectbox("Previous Campaign Outcome", [
    "nonexistent", "failure", "success"
])

st.header("Economic Indicators")

emp_var_rate = st.number_input(
    "Employment Variation Rate",
    value=1.1,
    format="%.1f"
)

cons_price_idx = st.number_input(
    "Consumer Price Index",
    value=93.994,
    format="%.3f"
)

cons_conf_idx = st.number_input(
    "Consumer Confidence Index",
    value=-36.4,
    format="%.1f"
)

euribor3m = st.number_input(
    "Euribor 3 Month Rate",
    value=4.857,
    format="%.3f"
)

nr_employed = st.number_input(
    "Number of Employees",
    value=5191.0,
    format="%.1f"
)

input_data = pd.DataFrame({
    "age": [age],
    "job": [job],
    "marital": [marital],
    "education": [education],
    "default": [default],
    "housing": [housing],
    "loan": [loan],
    "contact": [contact],
    "month": [month],
    "day_of_week": [day_of_week],
    "campaign": [campaign],
    "pdays": [pdays],
    "previous": [previous],
    "poutcome": [poutcome],
    "emp.var.rate": [emp_var_rate],
    "cons.price.idx": [cons_price_idx],
    "cons.conf.idx": [cons_conf_idx],
    "euribor3m": [euribor3m],
    "nr.employed": [nr_employed]
})
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

if prediction == "yes":
    st.success("Prediction: Yes - The customer is likely to subscribe.")
else:
    st.error("Prediction: No - The customer is not likely to subscribe.")

