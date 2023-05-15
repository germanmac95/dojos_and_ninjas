from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo , ninjas
from flask_app.models import dojos


#every controller needs 2 routes. One to display the page and the other to process data!

@app.route("/ninjas", methods = ["POST"]) 
def create_ninja():
    data = {
    "first_name": request.form["first_name"], 
    "last_name": request.form["last_name"],
    "age": request.form["age"],
    "dojo_id" : request.form["dojo_id"],
    }
    Ninja.create_ninja(data)
    return redirect(url_for("showdojos"))


@app.route("/viewninja/")
def index():
    all_dojos = Dojo.get_all()

    return render_template("ninja.html", all_dojos = all_dojos)

#route for displaying the ninja that belongs to the dojo

@app.route("/dojo/<int:id>")
def dojos_and_ninjas(id):
    data = {
        "id": id
    }
    
    results = dojos.Dojo.get_ninja_with_dojo(data)
    print(len(results.ninjas_list))
    return render_template("ninjas_in_dojos.html", dojo_for_ninja = results)


