from flask import Flask, render_template, request, url_for, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
#DB
app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cannabis-legality-db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# table
class Legality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String, nullable=False)
    decriminalized = db.Column(db.Text, nullable=False)
    recreational = db.Column(db.Text, nullable=False)
    medical = db.Column(db.Text, nullable=False)
    transportation = db.Column(db.Text, nullable=False)
    cultivation = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    



#Flask views
@app.route('/')
def index():
    return render_template('index.html',**locals())

# GET requests to return all the info from Legality DB
@app.route('/api', methods=['GET'])
def get_data():
    table = Legality.query.all()
    # modifying how information will display in view once jsonified
    d = {row.state:[{"Decriminalized":row.decriminalized},{"Recreational":row.recreational},{"Medical":row.medical},{"Transportation":row.transportation},{"Cultivation":row.cultivation},{"Notes":row.notes}] for row in table}
    return jsonify(d)
    

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        req = request
        return render_template("form.html", req=req)
    else:
        req = request
        return render_template("form.html")
    

app.run(debug=True)