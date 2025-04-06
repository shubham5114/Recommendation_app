import streamlit as st
from streamlit_lottie import st_lottie
import requests


def animation_call():

    url = requests.get(
        "https://lottie.host/fd53e292-06c0-4390-953c-1a9251cadb88/UBuRn7TaTu.json"
    )
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        st.write("Error in URL")

    st_lottie(
        url_json,
        # change the direction of our animation
        reverse=True,
        # height and width of animation
        height=400,
        width=400,
        # speed of animation
        speed=1,
        # means the animation will run forever like a gif, and not as a still image
        loop=True,
        # quality of elements used in the animation, other values are "low" and "medium"
        quality="high",
        # THis is just to uniquely identify the animation
        key="Hello",
    )
