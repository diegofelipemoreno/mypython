import urllib.request
import pdb
from htmldom import htmldom
from selenium import webdriver

class SearchStringOnDom:
    def __init__(self, list_urls):
        self.list_urls = list_urls
        self.dict_status_urls = {}

    def set_error_codes_dict(self):
        """
            Sets error codes dictionary from url list.
        """
        for index, url in enumerate(self.list_urls):
            req = urllib.request.Request(url)
            self.progress_msg(index, url)

            try:
                urllib.request.urlopen(req)
            except urllib.request.HTTPError as e:
                status_code = e.code
                if status_code in self.dict_sbogota2018tatus_urls:
                    self.dict_status_urls[status_code].append(url)
                else:
                    self.dict_status_urls[status_code] = [url]
    
    def progress_msg(self, index, url):
        """
            Shows the progress for each url.
        """
        list_urls_length = len(self.list_urls) -1

        if index:
            print("{0} of {1}: {2}".format(index, list_urls_length, url))
        else:
            print("-" * 50)
            print("Checking for status code error on urls: ")

    def getDom(self):
        """ 
            Get DOM form url provided.
        """
        for url in self.list_urls:
            pass
        driver = webdriver.Chrome()
        
        browser = webdriver.Firefox()
        
    def process(self):
        self.getDom()

if __name__ == "__main__":
    list_test_urls = ["https://developer.android.com/",
                      "https://httpstat.us/500",
                      "https://httpstat.us/522",
                      "https://www.android.com/intl/fr_fr/enterprise/management/s",
                      "https://www.android.com/versions/pie-9-0/s",
                      "https://developer.android.com/",
                      "https://wellbeing.google/tools/?utm_source=android&utm_medium=referral&utm_campaign=android_hero",
                      "https://www.blog.google/technology/safety-security/your-android-phone-is-a-security-key/",
                      "https://wellbeing.google/tools/?utm_source=android&utm_medium=referral&utm_campaign=android_hero",
                      "https://www.blog.google/technology/safety-security/your-android-phone-is-a-security-key/",
                      "https://developer.android.com/",
                      "https://developer.android.com/",
                      "https://developer.android.com/studio",
                      "https://source.android.com/",
                      "https://androidenterprisepartners.withgoogle.com/",
                      "https://blog.google/products/android/",
                      "https://www.blog.google/press/",
                      "https://www.blog.google/press/",
                      "https://wearos.google.com/#hands-free-help",
                      "https://support.google.com/android/?hl=en#topic=7313011",
                      "https://www.google.com/android/find?u=0",
                      "https://policies.google.com/?hl=en&gl=us",
                      "https://twitter.com/android/",
                      "https://www.instagram.com/android/",
                      "https://www.youtube.com/user/GoogleMobile/",
                      "https://www.facebook.com/AndroidOfficial/"]

    SearchStringOnDom(list_test_urls).process()
        