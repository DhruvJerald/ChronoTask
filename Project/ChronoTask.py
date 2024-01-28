import base64
import streamlit as st

st.set_page_config(
    page_title="ChronoTask",
    page_icon="⌚"
)

def set_background(png_file):
    b64 = base64.b64encode(open("1567666.png", 'rb').read()).decode()

    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % b64

    st.markdown(page_bg_img, unsafe_allow_html=True)
background_image_url = "/1567666.png"
set_background(background_image_url)

col1, col2, col3 = st.columns([2, 5, 5])
col1.image("OIG3-removebg-preview.png", width=100)
col2.title("ChronoTask")
col3.text(  "Clock in, Power Up.")

x = st.text_input("Enter your name")
y = st.text_input("Enter Age")
z = st.text_input("Enter Personal Email Address")
next_page_button_clicked = st.button("Go to Next Page")
if not (x and y and z):
    st.sidebar.warning("Please fill out all the required fields before proceeding.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("# Sidebar Navigation Disabled")
    st.sidebar.markdown("Please fill out the form to enable navigation.")
else:
    if next_page_button_clicked:
        st.success("Navigate to the next page")
        st.balloons()
        st.error("Dont enter data again as it will change the values in the database.")

if x and y and z:
    st.sidebar.success("Select a page below")

import streamlit as st

