import os
import shutil
import logging
import datetime
import tempfile
import unittest

from os.path import join as j

import iaTorrent

# don't let < ERROR clutter up test output
logging.basicConfig(level=logging.ERROR)


class TestiaTorrent(unittest.TestCase):

  def setUp(self):
    self.tmpdir = '/tmp/iaTorrent'
    if not os.path.exists(self.tmpdir):
      os.makedirs(self.tmpdir)

  def test_download_torrents(self):
    feed = 'http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=identifier+desc&sort%5B%5D=&sort%5B%5D=&rows=1&page=1&output=json'
    downloadDir = self.tmpdir
    torrent = iaTorrent.download_torrents(feed, downloadDir)

    # Check and see if we've connected, and downloaded a torrent
    self.assertTrue(os.path.isfile(j(self.tmpdir, 'zunhushishihua00chen.torrent')))

  def tearDown(self):
    if os.path.isdir(self.tmpdir):
      shutil.rmtree(self.tmpdir)

if __name__ == '__main__':
    unittest.main()
