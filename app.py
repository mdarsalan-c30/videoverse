import streamlit as st
import yt_dlp as youtube_dl
import os

def get_video_info(url):
    """Fetches video information and available formats."""
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        return info_dict['title'], [(f['format_id'], f.get('format_note', '')) for f in formats]

def download_video(url, format_id):
    """Downloads the video in the specified format."""
    output_dir = "/tmp"  # Use a temporary directory
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': format_id,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = os.path.join(output_dir, f"{info_dict['title']}.{info_dict['ext']}")
    
    return video_file

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube URL:")
if url:
    title, formats = get_video_info(url)
    st.write(f"Available formats for **{title}**:")
    format_options = [f"{fid}: {note}" for fid, note in formats]
    
    selected_format = st.selectbox("Select video resolution:", format_options)

if st.button("Download"):
    if url and selected_format:
        format_id = selected_format.split(":")[0]  # Get the format ID from the selected option
        try:
            video_file = download_video(url, format_id)
            with open(video_file, "rb") as f:
                st.download_button(
                    label="Download Video",
                    data=f,
                    file_name=os.path.basename(video_file),
                    mime="video/mp4"
                )
            st.success("Video downloaded successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid URL and select a resolution.")
