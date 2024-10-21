import streamlit as st
from connection import create_connection
from PIL import Image, ImageOps
from io import BytesIO
import pandas as pd


def image_processing(image_bytes):
    img = BytesIO(image_bytes)
    img = Image.open(img)
    img = ImageOps.fit(img, size=(150, 150))
    return img


def patient_history():
    cnic = st.text_input("Enter Patient's CNIC", max_chars=13)
    if st.button("Search"):
        conn = create_connection()
        mycursor = conn.cursor()
        sql = "select * from patient_info where cnic = %s"
        mycursor.execute(sql, (cnic,))
        result = mycursor.fetchall()
        if result:
            st.subheader('CNIC')
            st.write(result[0][1])
            st.subheader('Name')
            st.write(result[0][2])
            i=1
            for row in result:
                st.subheader("Record : {} ".format(i))
                st.subheader('Submission')
                st.write(row[7])
                st.subheader("Patient's CFI")
                image_bytes = row[3]
                if image_bytes:  
                    image = image_processing(image_bytes)
                    st.image(image)
                else:
                    st.write("Image not found in the database.")
                st.subheader("Predicted's Disease")
                st.write(row[4])
                st.subheader("Doctor's Remarks")
                st.write(row[5])
                st.subheader("Prescribed Medicine")
                st.write(row[6])
                i+=1

        else:
            st.warning('No record found', icon="⚠️")
