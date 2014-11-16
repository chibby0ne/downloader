#!/usr/bin/env python
""" downloads all files of a given format from webpage and stores it in location 

downloader uses wget to download the source code of the webpage, and stores the links 
in a a string and filters the links that contain the type of format specified into array
which it then downloads using wget again
"""

import os
import sys
import subprocess
import pages

'''
__author__ = "Antonio Gutierrez"
__copyright__ = "Copyright 2014, Antonio Gutierrez"
__credits__ = ["Antonio Gutierrez"]

__license__ = "GPL"


'''

# check CLAs
if len(sys.argv) != 4:
    print "Correct use is: ./down pagename format foldername"
    sys.exit(0)


# storing the webpage, format, and folder given as a CLA
url = sys.argv[1]
form = sys.argv[2]
folder = sys.argv[3]

# create directory if it doesn't exist yet
if os.path.isdir(folder) ==  False:
    os.mkdir(folder)

# downloading the webpage into file
subprocess.call(['wget', url,'-Oindex.html'])

# open file
fo = open('index.html')

# write file contents to string
url_string =''
links = []

for line in fo:
    url_string += str(line)

# make a list of links from string
links = pages.store_all_links(url_string)

# close file
fo.close()

#remove page file
# subprocess.call(['rm', 'index.html'])
os.remove("index.html")


# search list of links for the format specified and create new list with relevant links
my_links = []

for link in links:
    if link.find(form) != -1:
        if url.find("wikipedia"):               
            part = url.rfind('/')
            link = url[:url.rfind('/', 0, part)] + link
        elif url.find("google.com"):            # wget throws ERROR 403 Forbidden
            begin = link.find("imgurl=")
            end = link.find("&amp;")
            link = link[begin:end]
        elif link.find("http") == -1 or link.find("www") == -1:
            link = url + link
        my_links.append(link)


# download files with format specified and save them in folder specified as CLA
for link in my_links:
    subprocess.call(['wget', '-P', folder, link])
