#https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests 
page = requests.get("https://www.nytimes.com/")
#print(page.content)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#print(soup.find_all('h3')[5].get_text())
print(soup.find_all(class_='indicate-hover'))
