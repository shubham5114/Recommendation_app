import streamlit as st
from style import white_green_text_css


def about_section():
    st.markdown(white_green_text_css, unsafe_allow_html=True)
    styled_about_text = """
        
        # About CineGenius:
        Unlock Your Next Favorite Adventure with CineGenius! Dive into a world where movies, books, and cutting-edge skills recommendations are perfectly tailored to your tastes.
        """
    # Movie Recommendation System with Live Chat
    about_text = """
        
        ### Key Features:
        - **Diverse Recommendations:** From blockbuster movies to must-read books and advanced learning skills, CineGenius covers all your entertainment and educational needs.
        - **Interactive Experience:** Engage in live chats with our intelligent system that listens, responds, and even speaks to you, making your interaction delightfully seamless.
        - **Live Chat Interaction:** Our unique live chat feature allows you to communicate with CineGenius:. Type your queries or speak, and CineGenius: responds in style.
        - **Audio Feedback:** CineGenius: not only writes responses but also speaks to you, making the interaction more immersive.
        
        ### How It Works:
        1. **Recommendation Engine:** Our powerful recommendation engine analyzes your watching history and preferences.
        2. **Live Chat:** Engage in real-time conversations with CineGenius:. Ask for recommendations, movie trivia, or just chat about films.
        3. **Audio Responses:** Enjoy the experience of CineGenius: responding to you with both written and spoken words.
        4. Simply enter your current interests, and CineGenius uses sophisticated algorithms to analyze your preferences and suggest content and skills that you are bound to love. 
        5. Whether you're in the mood for a gripping drama, an inspiring read, or a skill that boosts your career, CineGenius is here to guide you every step of the way.
        
        ### Experience CineGenius: Today!
            Step into the future of personalized recommendations with CineGenius. Start your journey through the pages and screens of new discoveries that are as unique as you are. 
            Explore CineGenius now and let your next favorite adventure find you!
    """
    # Render the styled about section
    # Render the about text
    st.markdown(styled_about_text, unsafe_allow_html=True)
    st.markdown(about_text, unsafe_allow_html=True)
