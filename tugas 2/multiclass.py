# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<html><body><div class="class1">'
#                      '</div><div class="class2"></div>'
#                      '<div class="class3"></div></body></html>', 'html.parser')

# soup.findAll(True, {'class': ['class1', 'class2']})

#----------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import os
import fungsi_create_directory
import requests

def main_scraper(url, directory):
    fungsi_create_directory.create_directory(directory) #memanggil fungsi create_directory dari file fungsi_create_directory.py
    source_code = requests.get(url) 
    source_text = source_code.text
    soup = BeautifulSoup(source_text, 'html.parser')

    articles = soup.find_all("h3", {'class': 'article__title article__title--medium'})
    articles2 = soup.find_all(True, {'class': ['row article__wrap__grid--flex col-offset-fluid mt2']})  # Penulisan Multiple class

    for article in articles:
        print("URL  : " + article.a.get("href")) 
        print("Judul1 : " + article.text)
        print()

    for article2 in articles2:  
        print("URL2 : " + article2.a.get("href"))
        print("Judul2 : " + article2.text)
        print()

main_scraper("https://tekno.kompas.com/gadget", "Hasil")
