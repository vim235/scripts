#!/usr/bin/python
#coding: utf-8

import sys 
import os 
import urllib2 
from BeautifulSoup import BeautifulSoup 

kb = 1024
block_size = kb * 300000

url = raw_input("url: ")
soup = BeautifulSoup(urllib2.urlopen(url).read())
u"""
flashvars split
flv_url 
"""
flashvars = dict([(s[0], urllib2.unquote(s[1])) for s in map(lambda \
        x:x.split("="), soup.find("embed").get("flashvars").split("&"))])
#for k, v in flashvars.items():
#    print k, "=>" , v

save_dir = " "              # input the name of the directory
filename = (flashvars['linkurl'].split('/')[-1]) + '.flv'
video_file = None
for i in xrange(2):
    try:
        filepath = os.path.join(save_dir, filename)
        video_file = open(filepath, "wb")
    except(OSError, IOError):
        if filename.startswith(video_id):
            sys.exit("Error: unable to open %s for writing" % \
                    os.path.abspath(filepath))
        else:
            filename = video_id + ".flv"

#Download video data
try:
    response = urllib2.urlopen(flashvars['flv_url'])
    """
    total = response.info().getheader("content-length")
    total = to_k(int(total))
    total_width = len(str(total))
    downloaded = 0
    """
    while True:
        video_data = response.read(block_size)
        if not video_data: break
        video_file.write(video_data)
except urllib2.URLError, e:
    url_error("\nError: unable to download video data", e)
finally:
    video_file.close()

        
