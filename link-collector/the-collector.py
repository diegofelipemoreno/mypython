from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
import pdb

#pdb.set_trace()
LINK_REGEX = re.compile(
    "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>"
    )
HTML_PATH_REGEX = re.compile(
    "^[[a-zA-Z0-9_.-].+\.html"
)

class LinkCollector:
    def __init__(self, url):
        self.url = "http://" + urlparse(url).netloc
        self.data_collected = {}

    def collect_links(self, list_path=["/"]):
        full_url = ""
    
        list_path.append("/")
        for path in list_path:
            full_url = self.url + path
            page = str(urlopen(full_url).read())
            links = LINK_REGEX.findall(page)
            self.data_collected.setdefault(path, self.normalize_url(path, links))
         
    def normalize_url(self, path, links):
        set_links = set()

        for link in links:
            if len(link) > 1:
                if "http://" in link or "https://" in link:
                    set_links.add(link)
                if link.startswith('/'):
                    set_links.add(self.url + link)
                else:
                    set_links.add(self.url + path)
                if link.startswith('#'):
                    set_links.add(self.url + '/' +  link)
                if re.match(HTML_PATH_REGEX, link):
                    set_links.add(self.url + '/' + link)
        return set_links

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def display(self):
        #print(self.data_collected.keys())

        for url, links in self.data_collected.items():
            page_name = url.split("/")[1]
            if not page_name:
                page_name = "index.html"
            print("Page {}: \n\t".format(page_name))
            for link in links:
                print("  {} \n\t".format(link))
            print(">"*30)


if __name__ == "__main__":
    my_links_collector = LinkCollector(sys.argv[1])
    my_links_collector.collect_links(sys.argv[2:])
    my_links_collector.display()





#LinkCollector("http://localhost:8000").collect_links()
#print(sys.argv, sys.argv[0], sys.argv[1], sys.argv[2])
'''
def show_result_(path= ""):
    collector.collect_links(path)
    for link in collector.collected_links:
        print(link) 

collector = LinkCollector(sys.argv[1])
try:
    #path = collector.collect_links(sys.argv[2])
    show_result_(sys.argv[2])
except IndexError:
    print("-- A path was not be setted, it will collect from index.html")
    show_result_()
'''