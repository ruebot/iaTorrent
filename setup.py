from setuptools import setup

description = \
    """
    This package can be used to snatch torrents for each collection object from a given Internet archive collection.
    """

setup(
    name = 'ia-torrent',
    version = '0.1.0',
    url = 'https://github.com/ruebot/ia-torrent',
    author = 'Nick Ruest',
    author_email = 'ruestn@gmail.com',
    py_modules = ['ia-torrent'],
    scripts = ['ia-torrent.py'],
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
