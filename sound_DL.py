#!/usr/bin/python
#coding: utf-8

from gdata import *
import gdata.youtube
import gdata.youtube.service
from pytube import YouTube
from pprint import pprint
import pafy

search_word = "bach herreweghe Matthaeus"        # Input the search words.
client = gdata.youtube.service.YouTubeService()

query = gdata.youtube.service.YouTubeVideoQuery()
query.vq = search_word  
query.start_index = 1  #　
query.max_results = 1  # the number of videos you want to get
query.racy = "include"  
query.orderby = "relevance"  

feed = client.YouTubeQuery(query)

L = []
for entry in feed.entry:
    
    link = str(LinkFinder.GetHtmlLink(entry))
    L.append(link.split('href="')[1].split('&')[0])

url = L[0]
video = pafy.new(url)

audiostream = video.audiostreams
audiostream[1].download()
