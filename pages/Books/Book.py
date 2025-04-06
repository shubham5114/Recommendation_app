import streamlit as st
import pickle as pk
import pandas as pd
from streamlit_lottie import st_lottie
from pages.Pages_style.pages_style import (
    get_books_css,
)


def Book_call():
    st.markdown(get_books_css(), unsafe_allow_html=True)  # 👈 Applying CSS

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.image("pages/Books/Images/book.jpg", width=400)
    with col2:
        st.write(" ")
    with col3:
        st.markdown(
            """
            <h1>Books Recommendation System</h1>
            <p>Unleash the magic of endless reading with our Book Recommendation System! 
            Whether you're a seasoned bookworm or a curious newcomer, our system takes your 
            current literary crush and connects you with your next page-turner. Just tell us 
            the title of the book you're devouring, and we'll whisk you away on a new adventure 
            with a perfectly matched recommendation.</p>
            """,
            unsafe_allow_html=True,
        )

    def recommend(book_name):
        try:
            book_index = book_list[book_list["Book_Title"] == book_name].index[0]
        except IndexError:
            st.error("Book not found in the database.")
            return [], []

        l = sorted(
            (enumerate(similarity[book_index])), reverse=True, key=lambda x: x[1]
        )[1:7]

        recommended = []
        recommend_poster = []

        for i in l:
            recommended_book = book_list.iloc[i[0]]
            recommend_poster.append(recommended_book.Image)
            recommended.append(recommended_book.Book_Title)

        return recommended, recommend_poster

    book_lis = pk.load(open("pages/Books/Pickle_files/book.pkl", "rb"))
    book_list = pd.DataFrame(book_lis)
    similarity = pk.load(open("pages/Books/Pickle_files/book_similarity.pkl", "rb"))
    selected = st.selectbox("Enter Book", (book_list["Book_Title"]))

    if st.button("Recommend"):
        recommended, recommend_book_img = recommend(selected)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended[0])
            st.image(recommend_book_img[0])
        with col2:
            st.text(recommended[1])
            st.image(recommend_book_img[1])
        with col3:
            st.text(recommended[2])
            st.image(recommend_book_img[2])
        with col4:
            st.text(recommended[3])
            st.image(recommend_book_img[3])
        with col5:
            st.text(recommended[4])
            st.image(recommend_book_img[4])
