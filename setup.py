from setuptools import setup

description = \
    """
    This package can be used to snatch torrents for each collection object from a given Internet archive collection.
    """

setup(
    name = 'iaTorrent',
    version = '0.1.4',
    url = 'https://github.com/ruebot/ia-torrent',
    author = 'Nick Ruest',
    author_email = 'ruestn@gmail.com',
    py_modules = ['iaTorrent'],
    scripts = ['iaTorrent.py'],
    description = description,
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
