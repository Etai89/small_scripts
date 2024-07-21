import moviepy.audio.fx.all as afx
from pytube import YouTube
import time
import os
from moviepy.editor import *
from pydub import AudioSegment
import pathlib
import pyperclip

### THE FIRST FIXED VERSION COPY ONLY! ###

## FIRST PART:
## Downloading from youtube
copied_text = pyperclip.paste()
link = copied_text
# link = 'https://www.youtube.com/watch?v=CduA0TULnow'
yt = YouTube(link)
print("getting information from YouTube...")
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Artist: ", yt.author)
print("Description: ", yt.description)
print("Length: ", yt.length)
print("Publish Date: ", yt.publish_date)

print("Downloading", yt.title)
yd = yt.streams.get_highest_resolution()

# Get the path to the Downloads folder
downloads_folder = str(pathlib.Path().home() / "Downloads")

# Create the '432hz songs' folder if it doesn't exist
output_folder = os.path.join(downloads_folder, "new mp3")
os.makedirs(output_folder, exist_ok=True)

# Download the file to the 'Downloads' folder
yd.download(output_folder)
file_path = os.path.join(output_folder, yd.default_filename)
print(yt.title, "\nDownloaded successfully!")
time.sleep(1)

## SECOND PART:
## Converting mp4 to wav
print("start converting VIDEO to mp3")

# Define input and output file paths
input_file = file_path
output_file = os.path.join(output_folder, pathlib.Path(input_file).stem + '.mp3')

# Load video file
video = VideoFileClip(input_file)

# Extract audio from video
audio = video.audio

# Save audio to output file
audio.write_audiofile(output_file)

# Close video and audio files
video.close()
audio.close()
time.sleep(0.2)
os.remove(file_path)
print(f"Converted {input_file} to {output_file}")
print("\nVideo converted to MP3 successfully!!")
time.sleep(0.2)

# Open the MP3 file
if sys.platform.startswith('darwin'):  # macOS
    os.system('open ' + output_file)
elif os.name == 'nt':  # Windows
    os.startfile(output_file)
elif os.name == 'posix':  # Linux
    os.system('xdg-open ' + output_file)

