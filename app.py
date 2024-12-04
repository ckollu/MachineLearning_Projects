import streamlit as st
from PIL import Image
img =Image.open("SMS.png")
st.set_page_config(page_title ='Similar Movie Search', page_icon = img,
                   layout ='wide')
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
import re
from nltk.corpus import stopwords

from bs4 import BeautifulSoup
from tensorflow import keras

import tensorflow as tf   
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity

# Load css file

img_bg = """
<style>
[data-testid ="stAppViewContainer"] { 
background-color:lightgrey;
}
</style>
"""
st.markdown(img_bg, unsafe_allow_html=True)

df = pd.read_csv("movie_with_plots_1000.csv")

movies = []
for x in range(1000) : 
    movies.append(df["Movie Description"][x].strip()+" "+df["Plot"][x].strip())

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" 
model = hub.load(module_url)
print("USE model %s loaded" % module_url)
def embed(input):
    return model(input)

print("hi")
word_Embeddings = embed(movies)



page = st.sidebar.selectbox("SELECT ACTIVITY", ["INTRODUCTION","Similar Movie Search",])
st.sidebar.text(" \n")


if page=="INTRODUCTION":
    lgo, title = st.columns([1, 7])
    with lgo:
        img.putalpha(250) 
        st.image(img,width=125)
    with title:
        st.title("Similar Movie Search")
    st.header("Welcome to the Search Engine")
    st.video("Project.mp4")


if page == "Similar Movie Search":

    st.header("Similar Movie Search")


    raw_text = st.text_area("Enter Movie Plot")
    preprocessed_Text =[]
    if st.button("Analyze"):

        vector=embed([raw_text])
        vector=np.array(vector)
        score = []
        for i in range(len(word_Embeddings)):
            s = cosine_similarity(vector,np.array(word_Embeddings[i]).reshape(1,512))
            score.append(s[0][0])
        movie_ids = sorted(range(len(score)), key=lambda i: score[i], reverse=True)[:5]
        movie_ids_Scores = [score[x] for x in movie_ids]

        st.subheader("Similar Movies")
        
        i = 0
        for x in movie_ids:
        
            st.text(df["Movie Name"][x] +" "+" with similarity Score : "+ str(movie_ids_Scores[i]))
            i = i +1
