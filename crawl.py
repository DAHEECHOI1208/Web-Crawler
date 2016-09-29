__author__ = 'Taylor Condrack'
# module to get info from site and parse into text
import requests
from bs4 import BeautifulSoup
def get_articles(url):
# pulls info from the url page
    source_code = requests.get(url)
# converts info into text
    plain_text = source_code.text
# parses text
    soup = BeautifulSoup(plain_text, "html.parser")
# counter to three to print top three stories instead of all of them
    i=0
# findAll pulls all items of class headline text
    for article_name in soup.findAll('span', {'class': 'cd__headline-text'}):
        title = article_name.string
        i = i+1
        if i > 3: break
# prints string
        print(title)
#function calls for each separte url
get_articles('http://www.cnn.com/tech')
get_articles('http://www.cnn.com/travel')
get_articles('http://www.cnn.com/politics')
input("")