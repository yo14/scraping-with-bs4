import requests
import bs4

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})

print(html_doc.text)

