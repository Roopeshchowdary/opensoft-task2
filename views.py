from app import app
from flask import render_template

@app.route("/Home-page")
def logIn():

    return render_template("home-page.html")

@app.route("/Sign-In") 
def Register():

    return render_template("Sign-In.html")   
