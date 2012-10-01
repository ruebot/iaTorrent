# iaTorrent (Internet Archive torrent snatcher)

### Description

iaTorrent snatches all of the torrents for a given collection in the Internet Archive.

You'll need a json file for all the items in the collection with at least the title and identifier. You can get that from the Internet Archive [advanced search page](http://archive.org/advancedsearch.php). You'll need Query parameters as well. I grab the parameters from the 'All items (most recently added first) link on a collection page. 

Example:

[York University Library collection](http://archive.org/details/YorkUniversity)
Query parameters:

    (collection:yorkuniversity AND format:pdf) AND -mediatype:collection

Fields to return: identifier, title
Number of results: 2608 (number of items in the collection)

[Example](http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=2608&page=1&output=json)

### Installation

iaTorrent is a single-file python module that you can drop into your project as needed or you can install globally with:

    pip install iaTorrent

or

    cd ia-torrent
    sudo python setup.py install

### Usage

From python you can use the iaTorrent module to snatch a collection of torrents like this:

```python
import iaTorrent
torrent = iaTorrent.download_torrents('url_for_json', 'path_to_download_directory')
```

Or from the commandline:

    iaTorrent.py -f 'url_for_json' -d 'path_to_download_directory'


### Test suite

    python setup.py test

### Development

1. [Fork the repository](https://help.github.com/articles/fork-a-repo)
2. Do something awesome!
3. [Submit a pull request](https://help.github.com/articles/creating-a-pull-request) explianing what your plugin does

### License

![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")
