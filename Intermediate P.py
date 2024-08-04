import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.shadowfox.in/#'

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article titles (assuming they are in <h2> tags)
    articles = soup.find_all('p')

    # Print the titles of the articles
    for idx, article in enumerate(articles):
        print(f"{idx + 1}. {article.get_text()}")
else:
    print("Failed to retrieve the webpage.")

