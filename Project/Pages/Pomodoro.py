import base64
import streamlit as st
import time
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
import streamlit as st
import time

def pomodoro_timer(minutes):
    st.write(f"**Pomodoro Timer:** {minutes} minutes")
    progress_bar = st.progress(0)
    time_remaining = minutes * 60

    while time_remaining > 0:
        mins, secs = divmod(time_remaining, 60)
        st.write(f"Time remaining: {mins:02d}:{secs:02d}")
        time.sleep(1)
        progress_bar.progress((minutes * 60 - time_remaining) / (minutes * 60))
        time_remaining -= 1

    st.success("Pomodoro session completed!")

def main():
    st.title("Pomodoro Timer App")
    session_type = st.radio("Select session type", ["Pomodoro", "Short Break", "Long Break"])

    if session_type == "Pomodoro":
        pomodoro_timer(25)
    elif session_type == "Short Break":
        pomodoro_timer(5)
    elif session_type == "Long Break":
        pomodoro_timer(15)

if __name__ == "__main__":
    main()

def main():
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

    st.markdown(f'<div class="top-right"><img src="{image_url}" width="200" alt="Top Right Image"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

