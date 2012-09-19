#!/usr/bin/env python

import sys, os, re, urllib
from BeautifulSoup import BeautifulSoup

#if len(sys.argv) != 2:
#  print('Please verify RSS feed & download location')
#  sys.exit(-1)

feed = 'http://archive.org/services/collection-rss.php?collection=YorkUniversity&query=%28collection%3Ayorkuniversity%20AND%20format%3Apdf%29%20AND%20-mediatype%3Acollection' #sys.argv[1]      #user supplied RSS feed
download = '/tmp/ia-torrent'  #sys.argv[2]   #user supplied storage location

data = urllib.urlopen(feed)
soup = BeautifulSoup(data)
items = soup.findAll('item')

for item in items:
  title = item.find('title').string.strip()
  link = item.find('guid').string.strip()
  matchObj = re.match(r'https://archive.org/details/(.*)', link, re.M|re.I)
  identifier = matchObj.group(1)
  torrent = "https://archive.org/download/" + identifier + "/" + identifier +"_archive.torrent"
  urllib.urlretrieve(torrent, os.path.join(download, identifier + ".torrent"))
  print "Snatching: " + title + " from: " + torrent + "\n"
