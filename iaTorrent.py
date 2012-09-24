#!/usr/bin/env python

"""
iaTorrent snatches all of the torrents for a given collection in the Internet Archive.
"""

import sys
import os
import time
import json
import logging
import optparse
from urllib2 import Request, urlopen, URLError, HTTPError


class iaTorrentOptionParser(optparse.OptionParser):
  def __init__(self, *args, **opts):
    optparse.OptionParser.__init__(self, *args, **opts)

def _make_opt_parser():
  parser = iaTorrentOptionParser(usage="usage: %prog --feed 'url' --downloadDir '/path/to/download/directory'", version="%prog 0.1.3")
  parser.add_option("-f", "--feed", help="url to the json file", action="store", type="string", dest="feed")
  parser.add_option("-d", "--downloadDir", help="path to the download directory", action="store", type="string", dest="downloadDir")
  #(options, args) = parser.parse_args()

  return parser

# Set up logging
def _configure_logging():
  log_directory = os.path.join(downloadDir, 'logs')
  if not os.path.isdir(log_directory):
    os.mkdir(log_directory)
  logFile = os.path.join(downloadDir + '/logs', 'iaTorrent' + time.strftime('%y_%m_%d') + '.log')
  logging.basicConfig(filename=logFile, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def dlfile(url, identifier):
  # User agent
  request = Request(url, headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"})

  # Grab torrent link 
  try:
    f = urlopen(request)
    # Save file to download directory
    with open(os.path.join(downloadDir, identifier + ".torrent"), "wb") as local_file:
      local_file.write(f.read())

  # Error handling
  except HTTPError, e:
    logging.error("HTTP Error: %s %s \n", e.code, url)
  except URLError, e:
    logging.error("URL Error: %s %s \n", e.reason, url)

def download_torrents(feed, downloadDir):
 
  logging.info('Start')
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
    time.sleep(0.25)

  jsonData.close()
  logging.info('Finish')
  

if __name__ == '__main__':
  opt_parser = _make_opt_parser()
  opts, arg = opt_parser.parse_args()
  _configure_logging()
  log = logging.getLogger()

  rc = 0

  download_torrents(feed, downloadDir)

  sys.exit(rc)


