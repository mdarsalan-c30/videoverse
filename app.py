import gradio as gr
from pytube import YouTube

def download_video(url):
    if not url:
        return "Error: Please enter a valid URL."

    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download('/content')  # Save in Colab's content directory
        return f"Video '{video.title}' downloaded successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create a Gradio interface
iface = gr.Interface(
    fn=download_video,
    inputs=gr.Textbox(label="Enter YouTube URL", placeholder="https://www.youtube.com/watch?v=..."),
    outputs=gr.Textbox(label="Status", interactive=False),
    title="YouTube Video Downloader",
    description="Enter the URL of the YouTube video you want to download and press the button."
)

# Launch the app
iface.launch()
