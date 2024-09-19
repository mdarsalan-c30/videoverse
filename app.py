import streamlit as st
import yt_dlp as youtube_dl
import os

def download_video(url):
    # Set the output directory for the video
    output_dir = "/tmp"  # Use a temporary directory
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    # Download the video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = os.path.join(output_dir, f"{info_dict['title']}.{info_dict['ext']}")
    
    return video_file

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube URL:")
if st.button("Download"):
    if url:
        video_file = download_video(url)
        with open(video_file, "rb") as f:
            st.download_button(
                label="Download Video",
                data=f,
                file_name=os.path.basename(video_file),
                mime="video/mp4"
            )
        st.success("Video downloaded successfully!")
    else:
        st.error("Please enter a valid URL.")
