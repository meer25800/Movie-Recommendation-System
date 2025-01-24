import pickle
import streamlit as st
import requests


# Fetch poster using OMDb API
def fetch_poster(movie_id):
    api_key = "8fc5ee2e"  # Your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_id}&apikey={api_key}"
    response = requests.get(url).json()
    if "Poster" in response:
        return response["Poster"]
    return ""  # Return empty string if no poster is found


# Recommend movies function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].title))
    return recommended_names, recommended_posters


# Streamlit App setup
st.set_page_config(page_title="Movie Recommender System", page_icon="🎥", layout="wide")

# Page header
st.markdown(
    """
    <style>
        .header {
            font-size:50px;
            font-weight:bold;
            text-align:center;
            color:#FF4B4B;
        }
        .subheader {
            text-align:center;
            font-size:20px;
            font-weight:lighter;
            color:#3CAEA3;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="header">🎥 Movie Recommender System 🎬</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Discover Your Next Favorite Movie</div>', unsafe_allow_html=True)
st.markdown("---")

# Load pickled data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for movie selection
st.markdown("### Select a Movie to Get Recommendations")
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    st.markdown("### Recommended Movies")
    recommended_names, recommended_posters = recommend(selected_movie)

    # Display recommendations with cards
    for i in range(5):
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image(recommended_posters[i], use_container_width=True)  # Updated parameter
            with col2:
                st.subheader(recommended_names[i])
                st.markdown(f"*Enjoy this movie selected just for you!*")
            st.markdown("---")

