import pdb
import sys
import os
import re
from htmldom import htmldom

class GetUrlSitemap:
    def __init__(self, file):
        self.file = file
        self._sitemap_line_list = self.sitemap_line_list

    @property
    def sitemap_line_list(self):
        """Opens file and return a list of the file lines.
        Args:
            file: File to open.
        Returns:
            List of the file lines.
        """
        line_list = list()

        with open(self.file, "r") as file:
            for line in file:

                if "https://" in line and self._has_link_intl(line):
                    current_line = line.rstrip("\n")
                    #split_href_attr = current_line.split("https://")[1]
                    if current_line.split("https://")[1]:
                        line_cleaned = self._clear_tag_string(current_line.split("https://")[1])
                        #print(current_line.split("https://")[1])
                        print(line_cleaned)
                    line_list.append(line_cleaned)
    
        return line_list

    def output_result(self, list_urls):
        outname = "./assets/get-urls-sitemap-results.txt"

        with open(outname, "w") as outfile:
                for url in list_urls:
                    outfile.write("'" + url + "',\r\n")


    def _has_link_intl(self, tag_string):
        """Filter if link has intl path.

        Args:
           tag_string: Tag string provided.

        Returns:
        Boolean: True/False.
        """
        if "/intl/" in tag_string:
            return True

    def _clear_tag_string(self, tag_string):
        """Cleans tag provided to only tag content.

        Args:
           tag_string: Tag string provided.

        Returns:
        String: Tag content.
        """
        #clean = re.compile(".?>")
        clean = re.compile('.?>|\"|.?/>|</.+')
        text = re.sub(clean, "", tag_string)

        return text

    def find_element_on_urls(self, url_list):
        """Finds dom element on url provided.

        Args:
           url_list: List of urls.
        """
        dom = htmldom.HtmlDom( "http://www.android.com" ).createDom()
        print(dom)

    def process(self):
       #self.find_element_on_urls(["http://www.android.com"])
       result_list = self.sitemap_line_list
       self.output_result(result_list)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        GetUrlSitemap(arg).process()
        