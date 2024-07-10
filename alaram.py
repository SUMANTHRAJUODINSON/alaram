import streamlit as st
import datetime
import time
import pygame
import pyttsx3
from threading import Thread

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Initialize pygame mixer for sound
pygame.mixer.init()

# Streamlit UI
def main():
    st.title("Alarm Clock")
    st.subheader("Set Time")

    # Hour selection with AM/PM format
    hour = st.selectbox("Hour (AM/PM format)", [12] + list(range(1, 12)))
    am_pm = st.radio("AM/PM", ['AM', 'PM'])

    minute = st.selectbox("Minute", range(60))
    second = st.selectbox("Second", range(60))

    if st.button("Set Alarm"):
        if am_pm == 'AM':
            if hour == 12:
                hour_24 = 0
            else:
                hour_24 = hour
        elif am_pm == 'PM':
            if hour == 12:
                hour_24 = 12
            else:
                hour_24 = hour + 12

        # Calculate the alarm time based on AM/PM selection
        set_alarm_time = datetime.datetime.now().replace(hour=hour_24, minute=minute, second=second)
        set_alarm_time_str = set_alarm_time.strftime("%I:%M:%S %p")
        st.write(f"Alarm set for {set_alarm_time_str}")

        # Start threading the alarm
        threading_alarm(set_alarm_time)

# Threading and Alarm Function
def threading_alarm(set_alarm_time):
    def alarm():
        while True:
            current_time = datetime.datetime.now()
            print(current_time, set_alarm_time)

            # Check if current time has passed the alarm time
            if current_time >= set_alarm_time:
                print("Time to Wake up")
                pygame.mixer.music.load("sound.wav")
                pygame.mixer.music.play()
                speak_message("It's time to drink water")
                break

            time.sleep(1)

    t1 = Thread(target=alarm)
    t1.start()

# Function to speak a message
def speak_message(message):
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    main()
