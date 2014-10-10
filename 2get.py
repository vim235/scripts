#!/usr/bin/python
#coding: utf-8
 
import twopy
import datetime
import time

b = twopy.Board('')  #input url 

while 1:
    try:
        b.retrieve()
        L = [[0,0] for i in xrange(50)]
        for i in xrange(50):
            L[i][0] = b[i].since
            L[i][1] = b[i]
        L.sort()
        L.reverse()
        time.sleep(30)
    except:
        time.sleep(30)
        continue

    try:
        r = L[0][1].post(name=u"", mailaddr=u"",message="")
        if r[0] == twopy.STATUS_COOKIE:
            L[0][1].post(name=u"", mailaddr=u"", message=\
                    u" ", hidden=r[2])
            print L[0][1].title
            time.sleep(50)
    except:
        pass
