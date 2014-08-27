#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import re

TargetPath = '/home/denjo/"name of directory"'   # input name of directory

FileList = os.listdir(TargetPath)
k = len(FileList)
L = []
for f in FileList:
    TS = os.stat(f).st_mtime
    L.append([TS, f])

L.sort()

p = re.compile(".*jpg$")
q = re.compile(".*png$")
r = re.compile(".*gif$")
i = 1
j = 0
while j < k:
    if p.search("%s" % L[j][1]):
        os.rename("%s" % L[j][1], "%s.jpg" % str(i))
        i += 1
        j += 1
    elif q.search("%s" % L[j][1]):
        os.rename("%s" % L[j][1], "%s.png" % str(i))
        i += 1
        j += 1
    elif r.search("%s" % L[j][1]):
        os.rename("%s" % L[j][1], "%s.gif" % str(i))
        i += 1
        j += 1
    else:
        j += 1

