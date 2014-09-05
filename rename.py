#!/usr/bin/python

import os
import re

TargetPath = '/home/denjo/tumblr2'   # input name of directory

FileList = os.listdir(TargetPath)

L = []

p = re.compile(".*jpg$")
q = re.compile(".*png$")
r = re.compile(".*gif$")
 
for f in FileList:
    TS = os.stat(f).st_mtime
    L.append([TS, f])

M = []
for i in xrange(len(L)):
    if p.search(L[i][1]) or q.search(L[i][1]) or r.search(L[i][1]):
        M.append([L[i][0], L[i][1]])
M.sort()

i = 1
j = 0
while j < len(M):
    if p.search(M[j][1]):
        os.rename(M[j][1], "%s.jpg" % str(i))
        i += 1
        j += 1
    elif q.search(M[j][1]):
        os.rename(M[j][1], "%s.png" % str(i))
        i += 1
        j += 1
    elif r.search(M[j][1]):
        os.rename(M[j][1], "%s.gif" % str(i))
        i += 1
        j += 1
    else:
        j += 1
