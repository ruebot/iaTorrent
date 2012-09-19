# Internet Archive collection torrent snatcher

### Description

Grabs all of the torrents for a given collection.

You'll need a json file for all the items in the collection with at least the title and identifier. You can get that from the Internet Archive [advanced search page](http://archive.org/advancedsearch.php). You'll need Query parameters as well. I grab the parameters from the 'All items (most recently added first) link on a collection page. 

Example:

[York University Library collection](http://archive.org/details/YorkUniversity)
Query parameters:

    (collection:yorkuniversity AND format:pdf) AND -mediatype:collection

Fields to return: identifier, title
Number of results: 2608 (number of items in the collection)

[Example](http://archive.org/advancedsearch.php?q=%28collection%3Ayorkuniversity+AND+format%3Apdf%29+AND+-mediatype%3Acollection&fl%5B%5D=identifier&fl%5B%5D=title&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=2608&page=1&output=json)

### Usage

    python ia-torrent.py 'url_for_json' 'path_to_download_directory'

### License

![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")
