import base64
import streamlit as st
from streamlit_option_menu import option_menu
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

selected3 = option_menu(None, ["Settings"], 
    icons=['cast', 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "purple"},
        "nav-link-selected": {"background-color": "#19d9ff","color":"white"},
    }
)


on = st.toggle('Hardware Acceleration')

if on:
    st.write('Hardware Acceleration enabled')
def main():
    # Your image URL or file path
    image_url = "" 
    st.markdown(
        f"""
        <style>
            .top-right {{
                position: fixed;
                top: 100px;
                right: 100px;
            }}
        </style>
        """
    , unsafe_allow_html=True)

    st.markdown(f'<div class="top-right"><img src="{image_url}" width="50" alt="Top Right Image"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()