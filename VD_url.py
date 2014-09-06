#!/usr/bin/python
#coding: utf-8

from pytube import YouTube
from pprint import pprint

url = raw_input('url: ') # input the url you want.
yt = YouTube()
yt.url = url 
pprint(yt.videos)
print yt.filename
print yt.filter('mp4')[-1]

video = yt.get('mp4', '360p', 'Baseline')
video.download('/home/denjo/download')
