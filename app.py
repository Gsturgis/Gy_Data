from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/sqrt/<int:sqrt>')
def square(sqrt):
    import math
    square = int(math.sqrt(sqrt))
    return 'the square root of the route is {}'.format(square)

@app.route('/user/<username>')
def user(username):
    user = username
    return 'Hello! {} good afternoon.'.format(user)

@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("new", usr = user))
    else:
        return render_template('home.html')
        
    
@app.route("/<usr>")
def new(usr):
    return f"<h1>{usr}</h1>"

 
    
if __name__ == "__main__":
    app.run(debug=True)
    