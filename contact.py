import streamlit as st
import requests
from streamlit_lottie import st_lottie
from style import (
    header_css,
    form_title_css,
    social_icon_css,
    contact_info_css,
    copyright_css,
)


def contact_section():
    # ---------------------------------------------------Header----------------------------------------------------
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(header_css, unsafe_allow_html=True)
        st.markdown("# Contact Me")
    with c2:
        url = requests.get(
            "https://lottie.host/f4d597d4-dcb2-4192-a6ac-4eed6d41b422/YKnPIo8ExR.json"
        )
        if url.status_code == 200:
            st_lottie(
                url.json(),
                reverse=True,
                height=200,
                width=400,
                speed=1,
                loop=True,
                quality="high",
                key="contact",
            )
        else:
            st.error("Failed to load animation.")

    # ----------------------------------------------Form Section --------------------------------------------------
    st.markdown(form_title_css, unsafe_allow_html=True)
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/shubhampaliitr@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Details of your problem"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # ----------------------------------------------Social Media-------------------------------------
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
        unsafe_allow_html=True,
    )
    st.markdown(social_icon_css, unsafe_allow_html=True)

    def social_media_icons():
        icons = {
            "LinkedIn": "https://www.linkedin.com/in/shubham-kumar-78058924b/",
            "GitHub": "https://github.com/shubham5114",
            "Twitter": "https://twitter.com/your-twitter-profile",
            "Instagram": "https://www.instagram.com/shubham.5114/",
            "Facebook": "https://facebook.com/your-facebook-profile",
            "Discord": "https://discord.com/channels/@me",
        }
        return " ".join(
            f"""
            <a href="{link}" target="_blank" class="social-icon">
                <i class="fab fa-{platform.lower()}"></i>
            </a>
            """
            for platform, link in icons.items()
        )

    # --------------------------------------Contact Info + Icons-----------------------------------
    contact_info = """
    ### Contact Information
    - **Name:** Shubham Pal
    - **Email:** shubhampaliitr@gmail.com
    - **Phone:** +91- 7988192771
    """
    st.markdown(contact_info_css, unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("### Social Media Links")
        st.markdown(social_media_icons(), unsafe_allow_html=True)
    with col2:
        st.markdown(contact_info, unsafe_allow_html=True)

    # Footer
    st.markdown(copyright_css, unsafe_allow_html=True)
    st.markdown("### © 2023 Shubham Pal. All Rights Reserved.")
