import requests
from bs4 import BeautifulSoup

url = 'https://www.shadowfox.in/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('p')
    for idx, article in enumerate(articles):
        print(idx + 1,article.get_text())
else:
    print("Failed to retrieve the webpage.")

