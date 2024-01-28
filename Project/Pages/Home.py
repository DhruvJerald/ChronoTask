import streamlit as st
from prettytable import PrettyTable
import re
import base64
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

st.markdown(
    """
    <style>
        body {
            background-color: #f0f5f5; /* Light blue background */
            color: #333; /* Dark gray text color */
        }

        .stButton>button {
            background-color: #3498db; /* Blue button color */
            color: #fff; /* White text color on the button */
        }

        .stTextInput>div>div>input {
            background-color: #ecf0f1; /* Light gray input box */
        }

        .stText {
            color: #3498db; /* Blue text color */
        }

        .stMarkdown {
            color: #eee; /* white markdown text color */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

class Event:
    def __init__(self, title, duration, start_time=None, end_time=None):
        self.title = title
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time

class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def generate_timetable(self):
        timetable = PrettyTable()
        timetable.field_names = ["Time", "Event"]
        start_time = 8  
        current_time = start_time * 60  
        for event in self.events:
            if event.start_time is not None and event.end_time is not None:
                start_time_parts = list(map(int, filter(None, event.start_time.split(':'))))
                start_time_minutes = start_time_parts[0] * 60 + start_time_parts[1] if len(start_time_parts) == 2 else 0

                end_time_parts = list(map(int, filter(None, event.end_time.split(':'))))
                end_time = end_time_parts[0] * 60 + end_time_parts[1] if len(end_time_parts) == 2 else 0
            else:
                start_time_minutes = current_time
                end_time = current_time + event.duration * 60  
            start_time_str = f"{start_time_minutes // 60:02d}:{start_time_minutes % 60:02d}"
            end_time_str = f"{end_time // 60:02d}:{end_time % 60:02d}"
            timetable.add_row([f"{start_time_str} - {end_time_str}", event.title])
            current_time = end_time

        return timetable

def get_user_input():
    routines = st.text_area("Enter your daily routines and durations (e.g., studying-2hours-start_time08:00-end_time16:00):")
    routines_list = [routine.strip().split('-') for routine in routines.split(',')]

    if not routines_list:
        st.warning("Please enter your daily routines.")
        return []
    events = []
    for routine in routines_list:
        if len(routine) >= 2:
            title, duration_str = routine[0], routine[1]
            start_time, end_time = None, None

            for item in routine[2:]:
                if item.startswith("start_time"):
                    start_time = item[11:]
                elif item.startswith("end_time"):
                    end_time = item[9:]

            if duration_str.endswith("hours") and duration_str[:-5].isdigit():
                try:
                    duration_hours = int(duration_str[:-5])
                    events.append(Event(title, duration_hours, start_time, end_time))
                except ValueError:
                    st.warning(f"Invalid duration for activity '{title}': {duration_str}. Please use the format 'X hours.'")
            else:
                st.warning(f"Invalid duration format for activity '{title}': {duration_str}. Please use the format 'X hours.'")
        else:
            st.warning(f"Invalid routine format: {routine}. Each routine should have at least two elements.")

    return events

def main():
    st.title("Daily Timetable Generator")

    scheduler = Scheduler()

    user_events = get_user_input()

    for event in user_events:
        scheduler.add_event(event)

    if st.button("Generate Timetable"):
        timetable = scheduler.generate_timetable()
        st.header("Daily Timetable")
        st.write(timetable)

if __name__ == "__main__":
    main()
