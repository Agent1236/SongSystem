#!/usr/bin/env python
# coding: utf-8

# In[64]:

# get searched data info from youtube
from youtubesearchpython import VideosSearch
search = input("Search for a song - ")
videosSearch = VideosSearch(search, limit = 1)
data = videosSearch.resultComponents

# extract youtube url from api
x = data[0]
url = x['link']

# extract only audio
from pytube import YouTube
import os
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()

destination = "C:\\Users\\pgdew\\Music"

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
# %%
