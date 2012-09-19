#!/usr/bin/env python

import sys, os, re, urllib, time, json

#if len(sys.argv) != 2:
#  print('Please verify RSS feed & download location')
#  sys.exit(-1)

#feed = 'http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=50000&page=1&output=json'
#download = '/tmp/ia-torrent'
feed = sys.argv[1]
download = sys.argv[2]

jsonData = urllib.urlopen(feed)
data = json.load(jsonData)
items = data["response"]["docs"]

for item in items:
  identifier = item["identifier"]
  title = item["title"]
  torrent = "https://archive.org/download/" + identifier + "/" + identifier +"_archive.torrent"
  urllib.urlretrieve(torrent, os.path.join(download, identifier + ".torrent"))
  print "Snatching: " + title + " from: " + torrent + "\n"
  time.sleep(15)

jsonData.close()
