import streamlit as st
import yt_dlp
import os
import concurrent.futures

# Function definitions (download_video and merge_audio_video) go here

st.title("YouTube Video Downloader")

video_url = st.text_input("Enter YouTube Video URL:")
output_folder = "/content"

if st.button("Download"):
    if video_url:
        video_file, audio_file, output_file = download_video(video_url, output_folder)
        merge_audio_video(video_file, audio_file, output_file)
        st.success(f"Video downloaded and merged! [Download Here]({output_file})")
    else:
        st.error("Please enter a valid URL.")
