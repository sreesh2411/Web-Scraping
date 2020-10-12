from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

PATH=r"C:\Users\SREESH\Downloads\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(PATH)

products = []
prices = []

browser.get("https://www.flipkart.com/laptops/laptops~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g")

content = browser.page_source

soup = BeautifulSoup(content, 'lxml')

for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'}).text
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).text

    products.append(name)
    prices.append(price)

print(products)
print(prices)

df = pd.DataFrame({'Product_name': products, 'Price': prices})
df.to_csv('products.csv', index=False, encoding='utf-8')