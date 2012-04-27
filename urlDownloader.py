# urlDownloader.py --- 
# 
# Filename: urlDownloader.py
# Description: 
# Author: suyd
# Maintainer: 
# Created: 0 09 26 22:06:16 2010 (+0800)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# URL: 
# Keywords: 
# Compatibility: 
# 
# 

# Commentary: 
# 
# 
# 
# 

# Change Log:
# 
# 
# 
# 
# If you have any problem with this program , please feel free to contact
#      mail: suyd@kuxun.cn
#      gtalk: rtemslinux@gmail.com
#      msn:  suyedong@hotmail.com
#   
# 
# 

# Code:
import urllib2
import urllib
import os
import sys
def downloadUrl(url = ""):
    """
    """
    import httplib
    httplib.HTTPConnection.debuglevel = 1                         
    import urllib2
    request = urllib2.Request(url) 
    opener = urllib2.build_opener()                                   
    
    request.add_header('User-Agent',"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6)")
    feeddata = opener.open(request).read()
    return feeddata;

def Main():
    url = sys.argv[1]
    print downloadUrl(url )
    pass

if __name__ == "__main__":
    Main();
    pass
    
    



# 
# downloader.py ends here
