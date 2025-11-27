from bs4 import BeautifulSoup
import requests

# URL base pencarian Indeed
url = 'https://id.indeed.com/jobs'

# Parameter pencarian
params = {
    'q': 'Driver',   # kata kunci
    'l': 'Jakarta',         # lokasi
    'vjk': '48754c4c8dd04626'
}

# Header User-Agent yang kamu minta
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/142.0.0.0 Mobile Safari/537.36'
}

# Request halaman
res = requests.get(url, params=params, headers=headers)

# Cek status
print("Status code:", res.status_code)

# Parsing HTML
soup = BeautifulSoup(res.text, 'html.parser')

# Print HTML yang sudah diparse
print(soup.prettify())
