
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://www.detik.com/jatim/berita/indeks"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data_berita = []
    articles = soup.find_all("article")

    for article in articles:
        judul = article.find("h3")
        tanggal = article.find("span", attrs={"d-time": True})
        gambar = article.find("img")

        data_berita.append({
            "judul": judul.text.strip() if judul else "-",
            "tanggal": tanggal.text.strip() if tanggal else "-",
            "gambar": gambar["src"] if gambar else ""
        })

    return render_template("index.html", data=data_berita)

if __name__ == "__main__":
    app.run(debug=True)
