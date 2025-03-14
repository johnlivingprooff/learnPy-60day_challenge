import requests
from bs4 import BeautifulSoup
import os
import csv
import openpyxl

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"

res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
else:
    print("Failed to fetch webpage. Status code:", res.status_code)

# Creating our CSV file
with open("./WebData/fiction_books.csv", "w") as f:
    wrtr = csv.writer(f)

    wrtr.writerow(["Title", "Price"])

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        wrtr.writerow([title, price])
    print("✅ Successfully created the CSV file!")

# Creating our Excel file
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Fiction Books"

sheet.append(["Title", "Price"])

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a.text
    price = book.find("p", class_="price_color").text
    sheet.append([title, price])

workbook.save("./WebData/fiction_books.xlsx")
print("✅ Successfully created the Excel file!")
