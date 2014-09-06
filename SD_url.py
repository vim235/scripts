#!/usr/bin/python
#coding: utf-8

import pafy

url = raw_input('url: ') # Input the url you want dowonload.
video = pafy.new(url)

audiostream = video.audiostreams
audiostream[1].download()  #Input the directory you want to download in.
