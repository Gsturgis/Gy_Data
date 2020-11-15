from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Titania_(moon)"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

app = Flask(__name__)
@app.route('/')
def index():
    scrape = list(soup.find('table').stripped_strings)
    return render_template('index.html',**locals())

app.run(debug=True)