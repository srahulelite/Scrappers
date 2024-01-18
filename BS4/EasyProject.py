import requests
from bs4 import BeautifulSoup

site = "https://subslikescript.com/movies"
result = requests.get(site)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find("article", class_='main-article')
titles = box.find_all('a')
tit = []
for title in titles:
    tit.append(title['title'].split("'")[1])

file = 'a.txt'
with open(file, "a") as file:
    for k in tit:
        
file.close()

