import streamlit as st
from about import about_section
from contact import contact_section
from animation import animation_call
from style import dark_background
from style import nav_bar
from style import write_to_sidebar
from Speech_recognition import speechrecognition
from Speech_recognition import speak
from pages.Movie.Movies import Movie_call
from pages.Books.Book import Book_call
from pages.Skills.Advance_skills import Skills_call


st.set_page_config(layout="wide")
# import pickle as pk
# import pandas as pd
import requests
from streamlit_lottie import st_lottie

# import pyttsx3
# import speech_recognition as sr
# import streamlit_scrollable_textbox as stx

import subprocess

# Set background color to dark gray
dark_background()

# --------------------------------------------------------Nav Bar---------------------------------------------------------

selected = nav_bar()

if selected == "Home":
    c0, c1, c2 = st.columns([1, 2, 2])
    with c0:
        st.write("")
    with c1:
        # --------------------------------------------------------hello animation---------------------------------------------------------
        animation_call()

    # --------------------------------------------------------Domain call---------------------------------------------------------

    Domain_list = ["Choose Domain", "Movie", "Books", "Advanced Skills"]
    select = st.selectbox(
        "Enter Domain", Domain_list, index=0
    )  # Default selection is "Choose Domain"

    if select == "Choose Domain":
        st.write("Please select a domain to proceed.")
    elif select == "Movie":
        # subprocess.Popen(["streamlit", "run", "pages/1_Movie.py"])
        Movie_call()

    elif select == "Books":
        # subprocess.Popen(["streamlit", "run", "pages/2_Book.py"])
        Book_call()

    elif select == "Advanced Skills":
        # subprocess.Popen(["streamlit", "run", "pages/3_Advance_Skills.py"])
        Skills_call()

    with c2:
        styled_text = """
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f8f8f8;
                    color: #333;
                    line-height: 1.6;
                    margin: 20px;
                }

                h2 {
                    color: #76f5d6;
                    margin-top: 40px;
                }
            </style>

            ## About Us

            Welcome to CineGenius, your ultimate gateway to personalized recommendations!

            Whether you're in the mood for an enthralling movie, an engaging book, or looking to acquire a new skill, CineGenius is designed to cater to your unique tastes. Dive into a world where your next favorite adventure, story, or learning opportunity is just a recommendation away. Explore, discover, and transform your leisure and learning experiences with CineGenius today!
            """

        st.markdown(styled_text, unsafe_allow_html=True)

# ------------------------------------------------About-------------------------------------------------------

if selected == "About":
    about_section()

# ----------------------------------------------------contact me-----------------------------------------------------

if selected == "Contact Me":
    contact_section()

# -------------------------------------------------------SideBar---------------------------------------------------------
st.sidebar.title("Live Chat")

# -------------------------------------------------------------------------voice-------------------------------------------------------


# def mainExexution(query):
#     Query = str(query).lower()
#     if "hello" in Query:
#         speak("Hello Sir, How can I help you?")
#     elif "stop" in Query:
#         speak("Nice to meet you sir")
#         return True  # Indicate to stop the program
#     return False  # Continue the program


# while True:
#     Query = speechrecognition()
#     if mainExexution(Query):
#         write_to_sidebar("Program stopped.")
#         break


# ---------------------------------------------------------chat------------------------------------------------


def main_execution(query):
    """Process user input and generate responses."""
    query = query.lower()
    if "hello" in query:
        response = "Hello! How can I help you today?"
    elif "stop" in query:
        response = "It was nice chatting with you! Have a great day!"
        st.session_state.chatting = False
    else:
        response = "Sorry, I didn't understand that. Can you please repeat?"
    st.session_state.chat_history.append(f"You: {query}")
    st.session_state.chat_history.append(f"Pillu: {response}")


if __name__ == "__main__":
    # Initialize session state variables if not already present
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        st.session_state["chatting"] = True
        st.session_state["input_counter"] = 0

    write_to_sidebar()  # Display the chat history

    # Unique key for each input field
    unique_key = f"user_input_{st.session_state['input_counter']}"

    # Input field for user input
    user_input = st.sidebar.text_input("You:", key=unique_key)

    # Process input only if it is not empty
    if user_input:
        main_execution(user_input)
        # Increment the counter to ensure the next input widget has a new unique key
        st.session_state["input_counter"] += 1
        st.experimental_rerun()  # Rerun the app to update the chat log and reset the input box
