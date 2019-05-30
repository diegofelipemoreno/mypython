# Import libraries
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = "https://www.android.com/index.html"

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(1,len(soup.findAll('a'))): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    is_internal = re.match(r'^/(.+)?', link)
    download_url = link

    if is_internal:
        download_url = 'https://www.android.com'+ link

    #urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
    print(download_url, i, len(soup.findAll('a')))
    time.sleep(1) #pause the code for a sec
