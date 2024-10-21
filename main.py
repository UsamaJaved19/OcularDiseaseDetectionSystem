import streamlit as st

st.set_page_config(
    page_title="Multi-label Ocular Disease Classification"

)
if "disease" and "CFI" not in st.session_state:
    st.session_state.disease = ""
    st.session_state.CFI = ""


# program modules

from history import patient_history
from registration import form
from predictions import prediction
from PIL import Image, ImageOps
import time

st.title("Multi-Label Ocular Disease Detection System")
menu = ["Home", "Patient's registration", "Patients' Records"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    uploaded_file = st.file_uploader("Upload Color Fundus Image")
    if uploaded_file is not None:
        target_size = (150, 150)
        if st.button('Predict Disease'):
            st.session_state.CFI = uploaded_file.getvalue()
            image_upload = Image.open(uploaded_file)
            img = ImageOps.fit(image_upload, target_size)
            st.subheader("Patient's Color Fundus Image")
            st.image(img)
            disease = prediction(uploaded_file)
            st.session_state.disease = disease
            with st.spinner('Predicting your disease'):
                time.sleep(5)
            st.subheader("Result")
            st.info(f"Predicted Disease: {disease}", icon="ℹ️")
    else:
        st.warning('Enter your Color Fundus Image', icon="⚠️")
elif choice == "Patient's registration":
    st.subheader("Patient Registration")
    form()



elif choice == "Patients' Records":
    st.subheader("Patients' Records")
    patient_history()
