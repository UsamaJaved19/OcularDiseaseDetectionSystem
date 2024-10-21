import streamlit as st
from connection import create_connection



def form():
    with st.form(key="form"):
        cnic = st.text_input("Enter your CNIC", max_chars=13)
        name = st.text_input("Enter your name")
        remarks = st.text_input("Enter Doctor's Remarks")
        medicine = st.text_input("Enter Medicine")
        submitted = st.form_submit_button(label="Submit")
    if submitted == True:
        if not cnic or not name or not remarks or not medicine:
            st.warning("Fields are empty", icon="⚠️")

        elif len(cnic) != 13:
            st.warning("CNIC must be 13 digits", icon="⚠️")
        elif not cnic.isdigit():
            st.warning("CNIC must contain only digits", icon="⚠️")
        else:
            disease = st.session_state.disease
            CFI = st.session_state.CFI
            insert(cnic, name, CFI, disease, remarks,medicine)
            st.success('Patient Registered Successfully')



def insert(cnic, name, img, disease, remarks,medicine):
    conn = create_connection()
    mycursor = conn.cursor()
    sql = 'insert into patient_info(CNIC,Name,CFI,Predicted_Disease,Remarks,medicine) values(%s,%s,%s,%s,%s,%s)'
    values = (cnic, name, img, disease, remarks,medicine)
    mycursor.execute(sql, values)
    conn.commit()



