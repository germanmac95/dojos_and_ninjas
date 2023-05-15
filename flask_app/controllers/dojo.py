from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models import dojos


#every page needs 2 routes. one to display one to process data!
@app.route("/")
def showdojos():
    show_dojos = dojos.Dojo.get_all()
    print(show_dojos)
    return render_template("dojo.html", all_dojos = show_dojos)



#create 
@app.route("/process", methods = ["POST"])
def newdojo ():
    data = {
    "name": request.form["name"]
    }
    Dojo.create(data)
    return redirect(url_for("showdojos"))

