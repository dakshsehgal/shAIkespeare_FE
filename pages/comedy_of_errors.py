import streamlit as st
import time
import requests
from PIL import Image
from utils.audio import *
from utils.preprocessing import *

play, names = preprocess_play("assets/TheComedyOfErrors.csv")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
colors = ['violet', 'green', 'blue', 'red', 'orange']
name_to_color = {}
i = 0
for name in names:
    name_to_color[name] = colors[i]
    i += 1

play_title = "The Comedy of Errors"
play_author = "William Shakespeare"

st.markdown(f"<h1 style='text-align: center; color: white;'>{play_title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; color: white;'>{play_author}</h5>", unsafe_allow_html=True)

initial_img = Image.open('images/meeting.png')
ai_image = st.image(initial_img)

character_1 = st.markdown('')
quote_1 = st.markdown('')
character_2 = st.markdown('')
quote_2 = st.markdown('')
character_3 = st.markdown('')
quote_3 = st.markdown('')

url = 'http://127.0.0.1:5000/getDialog'

dialogues = [[character_1, quote_1], [character_2, quote_2], [character_3, quote_3]]

time.sleep(1)
counter = 0
prev_speaker = None
testing = Image.open('images/meeting.png')
for i in range(1, len(play)):
    ai_image.image(testing)
    rem = (i-1) % 3
    speaker, speech = play[i]
    sameSpeaker = speaker == prev_speaker
    curr_color = name_to_color[speaker]
    if not sameSpeaker:
        dialogues[rem][0].markdown(':' + curr_color + '[' + speaker +']')
        time.sleep(1)

    dataToSend = {
        "play_name": play_title,
        "line_no": counter
    }
    
    audio = requests.post(url, data = dataToSend)
    counter += 1
    
    # time.sleep(1)
    dialogues[rem][1].markdown(speech)
    autoplay_audio(audio.content)
    time.sleep(get_audio_duration(audio.content))
    prev_speaker = speaker
    if rem == 2:
        for dialog in dialogues:
            dialog[0].markdown('')
            dialog[1].markdown('')
    
