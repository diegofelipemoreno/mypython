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

                if "<loc>" in line and not self._has_link_intl(line):
                    current_line = line.rstrip("\n")
                    line_cleaned = self._clear_tag_string(current_line)
                    line_list.append(line_cleaned)
    
        return line_list

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
        clean = re.compile("<.*?>")
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
       self.find_element_on_urls(["http://www.android.com"])


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        GetUrlSitemap(arg).process()
        