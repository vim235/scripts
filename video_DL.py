#!/usr/bin/python
#coding: utf-8

from gdata import *
import gdata.youtube
import gdata.youtube.service
from pytube import YouTube
from pprint import pprint

search_word = raw_input('search word: ')  #  Input the search word
client = gdata.youtube.service.YouTubeService()


query = gdata.youtube.service.YouTubeVideoQuery()
query.vq = search_word  
query.start_index = 1  
query.max_results = raw_input('how many ?: ')  # the number of videos you want to get
query.racy = "include"  
query.orderby = "relevance"  

feed = client.YouTubeQuery(query)

L = []
for entry in feed.entry:
    link = str(LinkFinder.GetHtmlLink(entry))
    L.append(link.split('href="')[1].split('&')[0])

yt = YouTube()
yt.url = L[0] 
pprint(yt.videos)
print yt.filename
print yt.filter('mp4')[-1]
# download
video = yt.get('mp4', '360p', 'Baseline')
video.download('')  # Input the name of directory you want to get in.
