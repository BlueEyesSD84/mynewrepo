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
        "hobbies": "67 Mustang",
        "bio": "May name is Jimmy Smith and I am a Data Systems Analyst at Q2....."
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")