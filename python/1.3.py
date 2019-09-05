import urllib3

def download(url):
    return urllib3.urlopen(url).read()
