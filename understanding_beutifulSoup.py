'''
Understanding BeautifulSoup – A Beginner's Guide
BeautifulSoup is a Python library used to extract data from HTML and XML files.
It is commonly used for web scraping, which means gathering data from websites automatically.
In this script, we will see how BeautifulSoup is used to extract data from HTML files.

Why Use BeautifulSoup?
✅ Extract information from websites (e.g., product prices, headlines, weather data).
✅ Parse HTML easily (convert web pages into structured data).
✅ Navigate and search through HTML elements efficiently.
'''

# Step 1: Install BeautifulSoup
# To install BeautifulSoup, run the following command:
# pip install beautifulsoup4

# Step 2: Import Required Libraries
# First, we need to import the requests library to send HTTP requests to websites.
# Second, we import the BeautifulSoup class from the bs4 module.
# The following code snippet demonstrates this:

import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://books.toscrape.com"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    print("✅ Successfully fetched and parsed the webpage!")
else:
    print("❌ Failed to fetch webpage. Status code:", response.status_code)
