# import pickle as pk
# import pandas as pd
# import requests
# from streamlit_lottie import st_lottie
# from style import write_to_sidebar
# import pyttsx3
# import speech_recognition as sr
# import streamlit_scrollable_textbox as stx


# def speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty("voices")
#     ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#     engine.setProperty("voice", ID)
#     write_to_sidebar("")
#     write_to_sidebar(f"Pillu:  {text}")
#     write_to_sidebar("")
#     if text == "stop":
#         return True  # Indicate to stop the program
#     engine.say(text=text)
#     engine.runAndWait()
#     return False  # Continue the program


# def speechrecognition():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         write_to_sidebar("Listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)
#         try:
#             write_to_sidebar("Recognizing....")
#             query = r.recognize_google(audio, language="en")
#             write_to_sidebar("You:   " + query)
#             query = query.lower()
#             return query
#         except:
#             return ""
