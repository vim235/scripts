#!/usr/bin/python
#coding: utf-8

# You can download the videos you like from YouTube 

from pytube import YouTube
from pprint import pprint

url = raw_input('url: ') # Input the url you want.
yt = YouTube()
yt.url = url 
pprint(yt.videos)
print yt.filename
print yt.filter('mp4')[-1]

video = yt.get('mp4', '360p', 'Baseline')
video.download('') # Input the name of directory.
