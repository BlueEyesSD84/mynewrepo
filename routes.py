from flask import Flask, render_template

app = Flask(__name__)

#@app.get("/")
#def index():
#    return "<h1>Hello World!</h1>"

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about(): #Create a dictionary in the about.html page
    me = {
        "first_name": "Jimmy",
        "last_name": "Smith",
        "hobbies": "My 1967 Mustang",
        "bio": "May name is Jimmy Smith and I am a Data Systems Analyst at Q2,Inc.  I have been working at Q2 for almost 2 years.  My job is specifically to troubleshoot Python code designed for financial institutions.  The code is written in Python3 and the Database uses MySQL.  My job is good, pays well, but I am looking to move into the Web component of my company.  I enjoy designing and troubleshooting web issues."
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")