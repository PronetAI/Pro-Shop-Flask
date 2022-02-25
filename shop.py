from flask import Flask, render_template, request, redirect, flash
import random
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = '4t9hr4f9whw930345890*()u48jwrwfew4w(HF$Hqwd'

import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://oranges-pie:Q463gze75a0KyI63@cluster0.igpqd.mongodb.net/mySecondDatabase?retryWrites=true&w=majority")
mydb = client["Cluster1"]
collection = mydb.shopping_app


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == 'GET':
        return render_template('cricket.html')

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        doc = {'username': request.form['username'], 'pwd': request.form['pwd'],
               'bos': request.form['bos'],
               'email addr': request.form['email addr']}
        ind = mydb.users.find_one({'email addr': request.form['email addr']})
        if ind is None:
            mydb.users.insert(doc)
            flash("Account created successfully!")
            return redirect("/login")
        else:
            flash("This email is already taken up, please choose another one.")
            return redirect("/signup")

@app.route('/repl', methods=["GET", "POST"])
def repl():
    if request.method == 'GET':
        return render_template('repl.html')

@app.route('/youtube', methods=["GET", "POST"])
def youtube():
    if request.method == 'GET':
        return render_template('youtube.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        doc = {'title': request.form['title'], 'description': request.form['description'], 'price': request.form['price'],
               'unit': request.form['unit'], 'limit': request.form['limit'], 'img_url': request.form['img_url'],
               'ship': request.form['ship'], 'name': request.form['name'], 'email': request.form['email']}
        collection.insert(doc)
        return redirect("/")

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    return redirect("/page/1")

@app.route('/page/<pnum>', methods=['GET', 'POST'])
def pages(pnum):
    return ("Hi")
    pnum = int(pnum)
    if pnum == 1:
        Items = collection.find().limit(9)
    elif pnum == 2:
        Items = list(collection.find().limit(18))
        Items = Items[9:]
        print(Items)
    elif pnum == 3:
        Items = collection.find().limit(27)
        Items = Items[18:]
    else:
        Items = collection.find().limit(9)
    return render_template('buy.html', documents=Items)
if __name__ == '__main__':
    app.run(debug=True)
