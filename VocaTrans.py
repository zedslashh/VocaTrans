import streamlit as st
import whisper
import tempfile
import os

st.title("VocaTrans ↻ ◁ || ▷ ↺")

audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")
st.text("Whisper Model loaded")

if st.sidebar.button("Transcribe audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing audio")

        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name

        # Ensure ffmpeg is available
        if os.system("ffmpeg -version") == 0:
            # Transcribe the audio file
            transcription = model.transcribe(temp_file_path)
            st.sidebar.success("Transcription complete")
            st.markdown(transcription["text"])
        else:
            st.sidebar.error("FFmpeg is not installed. Please install it and try again.")
    
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play original audio file")
if audio_file:
    st.sidebar.audio(audio_file)
