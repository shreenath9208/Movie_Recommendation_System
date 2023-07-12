import pickle
import time

import pandas as pd
import requests
import streamlit as st
from PIL import Image

# This is actually the function for the finding the movies 



def fetch_poster(movie_id):
   response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=795ea3ac2a2a5e3eccc4700d85a2acc2".format(movie_id))
   data=response.json()
   return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
   



def Recommend(movie):
    movie_index=movie_data[movie_data['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x : x[1])[1:11]


    recomed_list=[]
    movies_poster=[]
    for i in movies_list:
        id= i[0]
        poster_id=movie_data.iloc[id].movie_id	
        movies_poster.append(fetch_poster(poster_id))
        recomed_list.append(movie_data.iloc[id].title)
    return recomed_list,movies_poster


# This is actually the code for the inserting the image



st.title('Welcome To The Movie Recommendation System')
# This is actually the line of the code for the getting the horizonatl line in the website
st.divider()

image = Image.open('movie_recommendation.jpg')
st.image(image)





# st.title('Welcome To The Movie Recommendation System')
# st.divider()
# st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
st.header('You Can Select Your Movies ')
st.divider()
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movie_data=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pkl","rb"))





selected_movie =st.selectbox(
    'Choose The Movie ',
 movie_data['title'].values )




st.divider()


# st.write('You selected:', option)

if st.button('Recommend'):
    names,posters=Recommend(selected_movie)
    col1, col2, col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
       st.text(names[1])
       st.image(posters[1])

    with col3:
       st.text(names[2])
       st.image(posters[2])
    
    with col4:
       st.text(names[3])
       st.image(posters[3])
    with col5:
       st.text(names[4])
       st.image(posters[4])
    
    with col6:
       st.text(names[5])
       st.image(posters[5])
    with col7:
       st.text(names[6])
       st.image(posters[6])
    with col8:
       st.text(names[7])
       st.image(posters[7])
    with col9:
       st.text(names[8])
       st.image(posters[8])
    with col10:
       st.text(names[9])
       st.image(posters[9])
       
    st.balloons()
   #  st.snow()
       


    
st.divider()

res = st.select_slider(
    'Have You Enjoyed Your Recommended Movie ',
    options=['Yes', 'No'])
st.write('Thank You For Your Valuable Time , Visit Again')



st.divider()


# import streamlit as st

with st.sidebar:
    with st.echo():
      st.write("You Have Reached Your Destination")

    with st.spinner("Loading..."):
        time.sleep(4)
    st.success("Done!")
    
    
    
    
    
    
    
    
    

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   # We cant use the tabs beacause of the st.tabs are only contains the string only
   
   
   
   
   
   
   
   
   
# if st.button('Recommend'):
#    names,posters=Recommend(selected_movie)
#    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([[names[0]],[names[1]],[names[2]],[names[3]],[names[4]],[names[5]],[names[6]],[names[7]],[names[8]],[names[9]]])

#    with tab1:
#       st.text(names[0])
#       st.image(posters[0],width=200)

   # with tab2:
   #    st.text(names[1])
   #    st.image(posters[1])

   # with tab3:
   #    st.text(names[2])
   #    st.image(posters[2])
    
   # with tab4:
   #    st.text(names[3])
   #    st.image(posters[3])
   # with tab5:
   #    st.text(names[4])
   #    st.image(posters[4])
    
   # with tab6:
   #    st.text(names[5])
   #    st.image(posters[5])
   # with tab7:
   #    st.text(names[6])
   #    st.image(posters[6])
   # with tab8:
   #    st.text(names[7])
   #    st.image(posters[7])
   # with tab9:
   #    st.text(names[8])
   #    st.image(posters[8])
   # with tab10:
   #    st.text(names[9])
   #    st.image(posters[9])