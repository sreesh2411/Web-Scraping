"""
from bs4 import BeautifulSoup

raw_html = open('demo.html').read()

html = BeautifulSoup(raw_html, 'html.parser')   #Convert raw html into a parser tree

for p in html.select('p'):
    #print(p.text)    #Obtain the content of the paragraph tag.
    if p['id'] == "first":
        print(p.text)



url = "https://fabpedigree.com/james/mathmen.htm"

raw_html = requests.get(url)         #Obtain raw html code
html = BeautifulSoup(raw_html.text, 'html.parser')

names = set()
for i, li in enumerate(html.select('li')):
    print(i, li.text)
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.codechef.com/problems/easy'
res = requests.get(url)

page = BeautifulSoup(res.text, 'lxml')

datatable_tags = page.select('table.dataTable')

datatable = datatable_tags[0]
prob_tags = datatable.select('a > b')

prob_names = [tag.getText().strip() for tag in prob_tags]

for i in prob_names:
    print(i)
