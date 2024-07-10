import streamlit as st
import datetime
import time
import winsound
import pyttsx3
from threading import Thread

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Streamlit UI
def main():
    st.title("Alarm Clock")
    st.subheader("Set Time")

    # Hour selection with AM/PM format
    hour = st.selectbox("Hour", [12] + list(range(1, 12)))
    am_pm = st.radio("AM/PM", ['AM', 'PM'])

    minute = st.selectbox("Minute", range(60))
    second = st.selectbox("Second", range(60))

    if st.button("Set Alarm"):
        set_alarm_time = f"{hour:02d}:{minute:02d}:{second:02d} {am_pm}"
        st.write(f"Alarm set for {set_alarm_time}")
        threading_alarm(set_alarm_time)

# Threading and Alarm Function
def threading_alarm(set_alarm_time):
    def alarm():
        while True:
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(current_time, set_alarm_time)

            if current_time == set_alarm_time:
                print("Time to Wake up")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                engine.say("It's time to drink water")
                engine.runAndWait()
                break

            time.sleep(1)

    t1 = Thread(target=alarm)
    t1.start()

if __name__ == "__main__":
    main()
