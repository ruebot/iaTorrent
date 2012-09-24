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


class TestTorrent(unittest.TestCase):

  def setUp(self):
    self.tmpdir = tempfile.mkdtemp()
    if os.path.isdir(self.tmpdir):
      shutil.rmtree(self.tmpdir)
    shutil.copytree('test-data', self.tmpdir)

  def tearDown(self):
    if os.path.isdir(self.tmpdir):
      shutil.rmtree(self.tmpdir)

  def test_main(self):
    feed = 'http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=5&page=1&output=json'
    downloadDir = self.tmpdir
    #identifier = '1714essaiphiloso00lockuoft'
    #url = "https://archive.org/download/" + identifier + "/" + identifier +"_archive.torrent"
    torrent = iaTorrent.main(feed, downloadDir)

    # Check and see if we've connected, and downloaded a torrent
    self.assertTrue(os.path.isfile(j(self.tmpdir, '1714essaiphiloso00lockuoft_archive.torrent')))

     

if __name__ == '__main__':
    unittest.main()
