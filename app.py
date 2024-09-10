import streamlit as st
import pickle
import pandas as pd

# Load the movie list and similarity matrix
movies_list = pickle.load(open('./movie_list.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

# Streamlit app
st.title('Movie Recommender System')

# Create a dropdown to select a movie
selected_movie = st.selectbox(
    'Select a movie from the dropdown',
    movies_list['title'].values
)

# Button to get recommendations
if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    st.write(f"Recommended movies similar to '{selected_movie}':")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")