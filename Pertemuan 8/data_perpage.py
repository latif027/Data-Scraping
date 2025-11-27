import requests
from bs4 import BeautifulSoup
import os

# Header (User-Agent Android Chrome 142 seperti permintaan Anda)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/142.0.0.0 Mobile Safari/537.36"
}

# URL pencarian Indeed
url = "https://id.indeed.com/jobs"

def get_total_pages():
    params = {
        'q': 'driver',
        'l': 'Jakarta',
        'vjk': '48754c48d0d04626'
    }

    # request ke halaman pencarian
    res = requests.get(url, params=params, headers=headers)

    # membuat folder 'temp' jika belum ada
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # menyimpan halaman HTML hasil scraping ke folder temp
    with open('temp/res.html', 'w+', encoding='utf-8') as outfile:
        outfile.write(res.text)

    # proses parsing
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())   # debug: menampilkan isi HTML hasil parsing


# Jalankan program
if __name__ == '__main__':
    get_total_pages()
