import streamlit as st
import csv
import time
import requests
import random

names = set()
def preprocess_play():
    out_str = []
    with open("TestPlay.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            names.add(row[0])
            out_str.append([row[0], row[1]])
    return out_str

play = preprocess_play()

colors = ['violet', 'green', 'blue', 'red', 'orange']
name_to_color = {}
i = 0
for name in names:
    name_to_color[name] = colors[i]
    i += 1

play_title = "Father's Day"

st.markdown("<h1 style='text-align: center; color: white;'>Father's Day</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>William Shakespeare</h5>", unsafe_allow_html=True)

character_1 = st.markdown('')
quote_1 = st.markdown('')
character_2 = st.markdown('')
quote_2 = st.markdown('')
character_3 = st.markdown('')
quote_3 = st.markdown('')

url = ''

dialogues = [[character_1, quote_1], [character_2, quote_2], [character_3, quote_3]]

time.sleep(1)
counter = 1
for i in range(1, len(play)):
    rem = (i-1) % 3
    item = play[i]
    curr_color = name_to_color[item[0]]

    time.sleep(1)
    dialogues[rem][0].markdown(':' + curr_color + '[' + item[0] +']')
    
    # x = requests.post(url, data = {play: play_title, count: counter})
    # api_text.text(x.content)
    # counter += 1

    time.sleep(1)
    dialogues[rem][1].markdown(item[1])
    
    time.sleep(1)
    if rem == 2:
        for dialog in dialogues:
            dialog[0].markdown('')
            dialog[1].markdown('')
