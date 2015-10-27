import requests
import urllib2
import urlparse
import re


class UrlDetails():
    """ Describe deatils of the web page of given url """

    def __init__(self, url):
        self.url = requests.get(url).url
        self.html = urllib2.urlopen(url).read()
        self.html_string = str(self.html)

    def get_domain_name(self):
        """ return the domain name of the url """
        domain_name = urlparse.urljoin(self.url, '/')
        return domain_name

    def get_title(self):
        """return tile of the page"""
        regex = re.compile('<title>(.*?)</title>', re.IGNORECASE | re.DOTALL)
        try:
            title = regex.search(self.html_string).group(1)
        except:
            title = ""
        return title

    def get_images(self):
        """return all images of the page"""
        imgurls = re.findall('img .*?src="(.*?)"', self.html)
        return imgurls

    def get_description(self):
        """return description of the pages"""
        regex = re.compile(
                '<meta .*?\scontent=["\'](.*?)["\']\s/>')
        des = regex.findall(self.html)
        if len(des) > 0:
            des = ','.join(des)
            return des

    @property
    def get_details(self):
        kwargs = dict()
        kwargs['domain'] = self.get_domain_name()
        kwargs['title'] = self.get_title()
        kwargs['description'] = self.get_description()
        kwargs['images'] = self.get_images()
        return kwargs
