import streamlit as st
import pickle as pk
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from pages.Pages_style.pages_style import get_movie_css  # ✅ Import CSS


# --------------------------------------------------------movie poster call---------------------------------------------------------
def Movie_call():

    st.markdown(get_movie_css(), unsafe_allow_html=True)  # ✅ Inject CSS

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.image("pages/Movie/Images/movie.jpg", width=400)
    with col2:
        st.write("")
    with col3:
        st.markdown(
            """
            # Movie Recommendation System

            Looking for your next movie night favorite but unsure where to start? 

            Try our Movie Recommendation System! Just pick a movie you enjoy, and our system will suggest similar films tailored to your tastes. It's like having a personal movie critic! Why waste time scrolling through countless options when your next great watch could be just a click away? Give it a try and revolutionize your movie-watching experience!
            """,
            unsafe_allow_html=True,
        )

    def poster(movie_id):
        response = requests.get(
            "https://api.themoviedb.org/3/movie/{}?api_key=e38b1e7fe3ec597dfcb5bb86217e9e94&language=en-US".format(
                movie_id
            )
        )
        data = response.json()
        return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]

    def recommend(movie_name):
        movie_index = movie_list[movie_list["title"] == movie_name].index[0]
        l = sorted(
            (enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1]
        )[1:6]
        recommended = []
        recommend_poster = []
        for i in l:
            movie_id = movie_list.iloc[i[0]].id
            # fetch poster from API

            recommend_poster.append(poster(movie_id))
            recommended.append(movie_list.iloc[i[0]].title)
            # print(recommend_movies_poster)
        return recommended, recommend_poster

    movie_list = pk.load(open("pages/Movie/Pickle_files/movie.pkl", "rb"))
    movie_list = pd.DataFrame(movie_list)
    similarity = pk.load(open("pages/Movie/Pickle_files/similarity.pkl", "rb"))
    selected = st.selectbox("Enter Movie", (movie_list["title"]))

    if st.button("Recommend"):
        recommend_movies_name, recommend_movies_poster = recommend(selected)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommend_movies_name[0])
            st.image(recommend_movies_poster[0])
        with col2:
            st.text(recommend_movies_name[1])
            st.image(recommend_movies_poster[1])
        with col3:
            st.text(recommend_movies_name[2])
            st.image(recommend_movies_poster[2])
        with col4:
            st.text(recommend_movies_name[3])
            st.image(recommend_movies_poster[3])
        with col5:
            st.text(recommend_movies_name[4])
            st.image(recommend_movies_poster[4])
