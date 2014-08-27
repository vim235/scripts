#!/usr/bin/python
#coding: utf-8

import urllib, Image
import re, sys, os.path

urllist = []
for i in range(1, num):                # num = number of pages of blogs you want to download
    urllist.append('http://'blog's name'.tumblr.com/page/%d' % i)  #input blog's name you want to download


p = re.compile("http://3\d.+_500.jpg|http://3\d.+_.*\d{2,}0.gif|http://3\d.+_500.png")
urlfile = open('urlfile1.py', 'w')
for i in xrange(len(urllist)):
    L = []
    html = urllib.urlopen(urllist[i])
    L = p.findall(html.read())
    for i in xrange(len(L)):
        urlfile.write(L[i])
        urlfile.write('\n')
urlfile.close()


def download(url):
    img = urllib.urlopen(url)
    if img:
        localfile = open(os.path.basename(url), 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()

f = open("urlfile1.py", "r")
f_lines = len([None for l in f])
f.close()

g = open("urlfile2.py", "r")      # urlfile2.py must be made in advance
g_lines = len([None for l in g])
g.close()


f = open("urlfile1.py", "r")
g = open("urlfile2.py", "r")

for i in xrange(f_lines):
    u1 = f.readline().rstrip()
    for j in xrange(g_lines):
        u2 = g.readline().rstrip()
        if u1 != u2:
            try:
                download(u1)
            except IOError:
                print u1 

f.close()
g.close()

f = open("urlfile1.py", "r")
g = open("urlfile2.py", "w")

for i in xrange(f_lines):
    g.write(f.readline())

f.close()
g.close()
