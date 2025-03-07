import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/example_webpage.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup.p.text)

    # price = soup.find("p", class_="price")
    # print(price.text)

    paragraphs = soup.find_all("p")
    list_of_paragraphs = []
    for p in paragraphs:
        list_of_paragraphs.append(p.text)
    
    print(list_of_paragraphs)