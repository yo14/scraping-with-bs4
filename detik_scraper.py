import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

print(soup)

