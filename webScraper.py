
from bs4 import BeautifulSoup
import requests

def websiteParser(url):
    site = requests.get(url)
    siteData = site.text.encode('utf-8').decode('ascii', 'ignore')
    soup = BeautifulSoup(siteData, "html.parser")
    title = str(soup.title)
    title = title.replace("<title>","").replace("</title>","")
    wholeText = title + " "
    for item in soup.find_all("p"):
        item = item.text
        item = item.encode('utf-8').decode('ascii', 'ignore')
        wholeText = wholeText + " " + item
    print(wholeText)
    return wholeText

websiteParser("https://www.businessinsider.com/whats-really-behind-x-googles-most-mysterious-company-2019-5")
