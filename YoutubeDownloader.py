'''
import yt_dlp as youtube_dl

video_url = input("enter url of youtube video:")
video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
filename = f"{video_info['title']}.mp3"
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename,
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])
print("Download complete... {}".format(filename))
'''

from __future__ import unicode_literals
import yt_dlp as youtube_dl
import ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    url=input("Enter Youtube URL: ")
    ydl.download([url])
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, 'output.wav')