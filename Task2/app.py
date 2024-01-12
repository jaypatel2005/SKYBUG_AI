import pickle as pk
import streamlit as st
import requests

movies = pk.load(open("movie_list.pkl", "rb"))
movie_list = movies['title'].to_list()

similarity = pk.load(open("similarity.pkl", "rb"))


def fetch_poster(movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=cb4a2f6cd39c02856e6637f1d3606f61&language=en-US").json()
    try:
        return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return None

def recommand(movie, n_movies=5):
    try:
        idx = movies[movies['title'] == movie.lower()].index[0]
    except IndexError:
        print("The movie name you entered is not available in our dataset")
        return
    except Exception as e:
        print(e)
        return
    
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x:x[1])
    
    recommanded = []
    posters = []
    
    for i in range(1, min(n_movies+1, movies.shape[0])):
        recommanded.append(movies.iloc[distances[i][0]]['title'])
        posters.append(fetch_poster(movies.iloc[distances[i][0]]['movie_id']))
    
    return recommanded, posters

st.title('Movie Recommander System')

selectedm = st.selectbox('which movie did you watched?', movie_list)

n_movies = st.number_input("Enter an integer:", step=1, value=5)

if st.button('Recommand'):
    names, posters = recommand(selectedm, n_movies)

    st.write("Recomended movies are ")

    for i in range(n_movies):
        st.write(f"{i+1}. {names[i]}")
        if posters[i] != None:
            st.image(posters[i], use_column_width=True)
        else:
            st.write(f"Poster can't be loaded for {names[i]}")