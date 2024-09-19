import streamlit as st
import yt_dlp as youtube_dl
import os

def download_video(url, download_path):
    if not url:
        st.error("Please enter a valid URL.")
        return

    if not download_path:
        st.error("Please select a download folder.")
        return

    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save video in selected folder
            'format': 'best',
        }

        # Download the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        st.success(f"Video downloaded successfully to {download_path}!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Create Streamlit app
st.title("YouTube Video Downloader")

# URL input
url = st.text_input("Enter YouTube URL:")

# Folder selection
download_path = st.text_input("Download folder:", os.getcwd())  # Default to current working directory
if st.button("Browse"):
    download_path = st.text_input("Enter download path manually:", os.getcwd())  # Placeholder for folder browsing

# Download Button
if st.button("Download"):
    download_video(url, download_path)
