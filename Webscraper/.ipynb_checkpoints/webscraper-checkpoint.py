from flask import Flask, render_template, request, url_for
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

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        req = request
        return render_template("form.html", req=req)
    

app.run(debug=True)