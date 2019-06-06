from html.parser import HTMLParser
from urllib import parse 


class LinkFinder(HTMLParser):

    def __init__(self):
         super().__init__() 
         self.links = set()

    def error(self, message):
        pass
   

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute, value) in attr:
                if attribute == 'href':
                    self.links.add(url)
    
    def page_links(self):
        return self.links


