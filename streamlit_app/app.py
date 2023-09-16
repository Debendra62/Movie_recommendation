import pickle
import streamlit as st
import pandas as pd

def recommend(movie):

    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommendation=[]
    for i in movies_list:
        recommendation.append(movies.iloc[i[0]].title)
    return  recommendation

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)
movies_list=movies['title'].values

st.title('Movies Recommendation System')
selected_movie_name=st.selectbox('Select your movie.',movies_list)
if st.button("Recommend", type="primary"):
    rec=recommend(selected_movie_name)
    for i in rec:
        st.write(i)
