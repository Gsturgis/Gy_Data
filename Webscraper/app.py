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
@app.route("/info", methods=["GET"])
def info():
    table = Legality.query.all()
    d=[]
    for row in table:
        h = row.state, row.decriminalized, row.recreational, row.medical, row.transportation, row.cultivation, row.notes
        d.append(h)
    
    return render_template("home.html", data = d)

#main page
@app.route('/')
def index():
    
    return render_template('index.html')

# GET requests to return all the info from Legality DB
@app.route('/api', methods=['GET'])
def get_data():
    table = Legality.query.all()
    # modifying how information will display in view once jsonified
    d = {row.state:[{"Decriminalized":row.decriminalized},{"Recreational":row.recreational},{"Medical":row.medical},{"Transportation":row.transportation},{"Cultivation":row.cultivation},{"Notes":row.notes}] for row in table}
    return jsonify(d)
    

    
if __name__ == '__main__':
    app.run(debug=True)