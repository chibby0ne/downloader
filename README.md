#Downloader

A simple python script that downloads all files of the given format from a website and stores it in the given directory. It uses wget for the back-end.

At the moment it requires that the given directory or path exists. It should work in all platforms provided they have the requirements.

## Requirements

* [Python 2](https://www.python.org/)
* [wget](https://www.gnu.org/software/wget/)

## Installation

``` bash
git clone https://www.github.com/chibby0ne/downloader
cd downloader/
```

(Optional) `export PATH=$PATH:$(pwd)` 

## Usage
```bash
downloader url format place_to_store_them
```
or if the path is not added to `PATH` variable:

```bash
./downloader url format place_to_store_them
```

## License 

This project is licensed under the [GNU GPLv2](LICENSE)

## Copyright 

Copyright (c) 2014 Antonio Gutierrez
