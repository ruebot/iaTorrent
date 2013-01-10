from setuptools import setup

import pandoc                  
pandoc.core.PANDOC_PATH = '/usr/bin/pandoc'

doc = pandoc.Document()        
doc.markdown = open('README.md').read()

description = \
    """
    This module can be used to snatch torrents for each collection object from a given Internet archive collection.
    """

setup(
    name = 'iaTorrent',
    version = '0.1.4',
    url = 'https://github.com/ruebot/ia-torrent',
    install_requires=['pyandoc'],
    author = 'Nick Ruest',
    author_email = 'ruestn@gmail.com',
    py_modules = ['iaTorrent'],
    scripts = ['iaTorrent.py'],
    description = description,
    long_description = doc.rst,
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
      'License :: Public Domain',
      'Intended Audience :: Developers',
      'Topic :: Communications :: File Sharing',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Filesystems',
    ],
)
