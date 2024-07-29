# VocaTrans-Audio transcription app
VocaTrans is a web application that leverages Whisper's speech-to-text model for transcribing audio files. Users can upload audio files in various formats, and the app provides real-time transcription while ensuring FFmpeg is available for processing.

**Libraries used**

1)Streamlit-Streamlit is a library used for creating interactive web applications in Python.
pip install streamlit

2)Whisper- Whisper is a library by OpenAI for automatic speech recognition (ASR).
pip install git+https://github.com/openai/whisper.git -q

3)FFmpeg-FFmpeg is a multimedia framework used for handling audio, video, and other multimedia files and streams.It is required to process and transcribe audio files.
  i)Download zip file of ffmpeg
  ii)Add bin path to environment variables

4)Pytorch-
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

**Implementing App**

1)Run the command-streamlit run VocaTrans.py

![Screenshot 2024-07-22 232204](https://github.com/user-attachments/assets/7c5c12f5-78a2-4536-a594-99803dd960cf)
