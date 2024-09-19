import streamlit as st
import yt_dlp as youtube_dl
import os

def get_video_info(url):
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        return [(f['format_id'], f['format_note']) for f in formats if 'format_note' in f]

def download_video(url, format_id):
    output_dir = "/tmp"  # Use a temporary directory
    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    # Download the video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = os.path.join(output_dir, f"{info_dict['title']}.{info_dict['ext']}")
    
    return video_file

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube URL:")
if url:
    formats = get_video_info(url)
    format_options = [f"{format_id} - {format_note}" for format_id, format_note in formats]
    
    selected_format = st.selectbox("Choose video resolution:", format_options)

    if st.button("Download"):
        format_id = selected_format.split(" - ")[0]
        video_file = download_video(url, format_id)
        with open(video_file, "rb") as f:
            st.download_button(
                label="Download Video",
                data=f,
                file_name=os.path.basename(video_file),
                mime="video/mp4"
            )
        st.success("Video downloaded successfully!")
