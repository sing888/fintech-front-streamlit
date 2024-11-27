import streamlit as st
import requests

url = 'https://lending-club-with-rf-flask-app.onrender.com/predict'

st.title("Loan Default Prediction")

loan_amnt = st.number_input('Loan Amount (e.g., 10000)', value=0, min_value=0, step=1, format="%d", key="1")
funded_amnt = st.number_input('Funded Amount (e.g., 10000)', value=0, min_value=0, step=1, format="%d", key="2")
term = st.selectbox('Term (e.g., 36 months)', ['-- Select an Option --', '36 months', '60 months'], key="3")
int_rate = st.number_input('Interest Rate (e.g., 13.56)', value=0.0, min_value=0.0, key="4")
installment = st.number_input('Installment (e.g., 500.0)', value=0.0, min_value=0.0, key="5")
grade = st.selectbox('Grade (e.g., A)', ['-- Select an Option --', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], key="6")
subgrade = st.selectbox('Subgrade (e.g., A1)', ['-- Select an Option --', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3', 'G4', 'G5'], key="7")
emp_length = st.text_input('Employment Length (e.g., 10 years)', placeholder="Enter employment length", key="8")
home_ownership = st.selectbox("Home Ownership (e.g., RENT)", ['-- Select an Option --', 'OWN', 'RENT', 'MORTGAGE', 'OTHER'], key="9")
annual_inc = st.number_input('Annual Income (e.g., 45000.0)', value=0.0, min_value=0.0, key="10")
ver_stat = st.selectbox("Verification Status (e.g., Verified)", ['-- Select an Option --', 'Verified', 'Source Verified', 'Not Verified'], key="11")
purpose = st.selectbox('Purpose (e.g., debt consolidation)', ['-- Select an Option --', 'debt consolidation', 'credit card', 'home improvement', 'major purchase', 'small business', 'car', 'wedding', 'medical', 'moving', 'vacation', 'house', 'renewable energy', 'educational', 'other'], key="12")
dti = st.number_input('DTI (Debt-to-Income Ratio, e.g., 18.45)', value=0.0, min_value=0.0, key="13")
delinq_2yrs = st.number_input('Delinquencies in 2 years (e.g., 1)', value=0, min_value=0, key="14")
earliest_cr_line = st.text_input('Earliest Credit Line (e.g., "Jan-1995")', placeholder="Enter date", key="15")
fico_range_low = st.number_input('FICO Credit Score Range Low (e.g., 650)', value=0, min_value=0, key="16")
fico_range_high = st.number_input('FICO Credit Score Range High (e.g., 700)', value=0, min_value=0, key="17")
inq_last_6mths = st.number_input('Credit Inquiries in last 6 months (e.g., 3)', value=0, step=1, format="%d", key="18")
mths_since_last_delinq = st.number_input('Months Since Last Delinquency (e.g., 6)', value=0, step=1, format="%d", key="19")
open_acc = st.number_input('Open Accounts (e.g., 5)', value=0, min_value=0, key="20")
pub_rec = st.number_input('Public Records (e.g., 0)', value=0, min_value=0, key="21")
revol_bal = st.number_input('Revolving Balance (e.g., 5000)', value=0, min_value=0, key="22")
revol_util = st.number_input('Revolving Utilities (e.g., 35.5)', value=0.0, min_value=0.0, key="23")
total_acc = st.number_input('Total Credit Accounts (e.g., 15)', value=0, min_value=0, key="24")
total_rec_prncp = st.number_input('Total Principal Received (e.g., 2500.0)', value=0.0, min_value=0.0, key="25")
total_rec_int = st.number_input('Total Interest Received (e.g., 150.0)', value=0.0, min_value=0.0, key="26")
last_pymnt_d = st.text_input('Last Payment Date (e.g., "Jan-1995")', placeholder="Enter date", key="27")
last_pymnt_amnt = st.number_input('Last Payment Amount (e.g., 450.0)', value=0.0, min_value=0.0, key="28")
last_fico_range_high = st.number_input('Last FICO Credit Score Range High (e.g., 700)', value=0, min_value=0, key="29")
last_fico_range_low = st.number_input('Last FICO Credit Score Range Low (e.g., 650)', value=0, min_value=0, key="30")

if st.button('Predict'):
    no_space = purpose.replace(' ', '_')

    payload = {
        'loan_amnt': loan_amnt,
        'funded_amnt': funded_amnt,
        'term': term,
        'int_rate': int_rate,
        'installment': installment,
        'grade': grade,
        'sub_grade': subgrade,
        'emp_length': emp_length,
        'home_ownership': home_ownership,
        'annual_inc': annual_inc,
        'verification_status': ver_stat,
        'purpose': no_space,
        'dti': dti,
        'delinq_2yrs': delinq_2yrs,
        'earliest_cr_line': earliest_cr_line,
        'fico_range_low': fico_range_low,
        'fico_range_high': fico_range_high,
        'inq_last_6mths': inq_last_6mths,
        'mths_since_last_delinq': mths_since_last_delinq,
        'open_acc': open_acc,
        'pub_rec': pub_rec,
        'revol_bal': revol_bal,
        'revol_util': revol_util,
        'total_acc': total_acc,
        'total_rec_prncp': total_rec_prncp,
        'total_rec_int': total_rec_int,
        'last_pymnt_d': last_pymnt_d,
        'last_pymnt_amnt': last_pymnt_amnt,
        'last_fico_range_high': last_fico_range_high,
        'last_fico_range_low': last_fico_range_low,
    }
    response = requests.post(url=url, json=payload)

    if response.status_code == 200:
        prediction = response.json().get('predicted_status')
        if prediction == 'non-default':
            st.success(f'Result: {prediction}')
        else:
            st.error(f'Result: {prediction}')
    else:
        st.error('Failed to retrieve prediction.')
        st.error(f"Error: {response.status_code}")
        st.error(f"Response Content: {response.text}")
