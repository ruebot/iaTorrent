#!/usr/bin/env python

import sys
import os
import time
import json
import logging
from urllib2 import Request, urlopen, URLError, HTTPError

if len(sys.argv) != 3:
  print("usage: ia-torrent 'url' '/path/to/download/directory'")
  sys.exit(-1)

downloadDir = sys.argv[2]

# Set up logging
log_directory = os.path.join(downloadDir, 'logs')
if not os.path.isdir(log_directory):
  os.mkdir(log_directory)
logFile = os.path.join(downloadDir, 'ia-torrent' + time.strftime('%y_%m_%d') + '.log')
logging.basicConfig(filename=logFile, level=logging.DEBUG)

#feed = 'http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=2608&page=1&output=json'

def dlfile(url, identifier):
  # User agent
  request = Request(url, headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"})

  # Download directory
  downloadDir = sys.argv[2]

  # Grab torrent link 
  try:
    f = urlopen(request)
    # Save file to download directory
    with open(os.path.join(downloadDir, identifier + ".torrent"), "wb") as local_file:
      local_file.write(f.read())

  # Error handling
  except HTTPError, e:
    logging.error("HTTP Error:", e.code, url + "\n")
  except URLError, e:
    logging.error("URL Error:", e.reason, url + "\n")

def main():
  
  feed = sys.argv[1]
  request = Request(feed, headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"})
  jsonData = urlopen(request)
  data = json.load(jsonData)
  items = data["response"]["docs"]

  for item in items:
    identifier = item["identifier"]
    title = item["title"]
    filename = identifier + ".torrent"
    items = data["response"]["docs"]
    url = "https://archive.org/download/" + identifier + "/" + identifier +"_archive.torrent"
    dlfile(url, identifier)
    print "Snatching: " + title + " from: " + url + "\n"
    time.sleep(0.5)

  jsonData.close()

if __name__ == '__main__':
  main()
