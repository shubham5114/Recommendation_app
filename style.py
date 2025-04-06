import streamlit as st
from streamlit_option_menu import option_menu


def dark_background():
    st.markdown(
        """
    <style>
    .css-17eq0hr {
        color: white;
        background-color: #1E1E1E;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def nav_bar():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Contact Me"],
        icons=["house", "question-circle-fill", "person-lines-fill"],
        menu_icon="cast",
        orientation="horizontal",
        styles={
            "container": {"padding": "10"},
            # "icon": {"color": "orange", "font-size": "25px"},
            # "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#37ad90"},
        },
    )

    st.markdown(
        "<h1 style='text-align: center;color: #f8f8f8;text-shadow: 2px 2px 8px #37ad90;'>Recommendation System</h1>",
        unsafe_allow_html=True,
    )
    return selected


def write_to_sidebar():
    """Display all chat messages in the sidebar with styling."""
    for message in st.session_state.chat_history:
        st.sidebar.markdown(
            f"""
            <div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; margin: 10px;">
                <span style="color: #3366cc; font-size: 18px; font-weight: bold;">{message}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


white_green_text_css = """
<style>
    h1 {
        color: #f8f8f8;
        text-shadow: 2px 2px 8px #37ad90;
    }
    h3{
        color: #37ad90;
        text-shadow: #f8f8f8;
    }
    p {
        color: #f8f8f8;
        font-size: 16px;
    }
</style>
"""

# style.py

header_css = """
<style>
    h1 {
        color: #f8f8f8;
        padding-left: 10px;
        text-shadow: 2px 2px 8px #CE4BC2;
    }
</style>
"""

form_title_css = """
<style>
    h3 {
        color: #f8f8f8;
        padding-left: 10px;
        padding-top: 100px;
        text-shadow: 2px 2px 8px #CE4BC2;
    }
    form {
        display: flex;
        flex-direction: column;
    }
    input, textarea {
        width: 100%;
        padding: 12px;
        margin: 10px 0;
        border-radius: 10px;
        border: none;
        background-color: #f0f0f0;
    }
    button {
        background-color: #CE4BC2;
        color: white;
        padding: 12px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    button:hover {
        background-color: #9b3092;
    }
</style>
"""

social_icon_css = """
<style>
    .social-icon {
        font-size: 30px;
        color: #3498db;
        margin: 0 10px;
        transition: color 0.3s;
        text-decoration: none;
    }
    .social-icon:hover {
        color: #e74c3c;
    }
</style>
"""

contact_info_css = """
<style>
    .contact-info {
        font-size: 18px;
        color: #f8f8f8;
        text-shadow: 2px 2px 8px #CE4BC2;
    }
</style>
"""

copyright_css = """
<style>
    .copyright {
        font-size: 16px;
        color: #f8f8f8;
        text-shadow: 2px 2px 8px #CE4BC2;
        margin-top: 20px;
    }
</style>
"""
