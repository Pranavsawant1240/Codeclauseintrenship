import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


r = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

title = soup.title

paras = soup.find_all('p')
print(paras)

print(soup.find('p') ) 

print(soup.find('p')['class'])

print(soup.find_all("p", class_="lead"))

print(soup.find('p').get_text())
print(soup.get_text())

anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)


elem = soup.select('.modal-footer')
print(elem)
elem = soup.select('loginModal')
print(elem)

 
