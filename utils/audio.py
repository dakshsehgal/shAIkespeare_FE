import base64
from io import BytesIO
import librosa
import streamlit as st


def get_audio_duration(audio_bytes, sr=22050):
    try:
        # Convert bytes to numpy array
        audio_array, _ = librosa.load(BytesIO(audio_bytes), sr=sr)

        # Calculate the duration in seconds
        duration_in_seconds = len(audio_array) / float(sr)

        return duration_in_seconds
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None

def autoplay_audio(data: any):
    b64 = base64.b64encode(data).decode()
    md = f"""
            <audio  autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
    st.markdown(
        md,
        unsafe_allow_html=True, )