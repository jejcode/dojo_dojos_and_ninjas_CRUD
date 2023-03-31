from flask_app import app # import app to manage routes
from flask import render_template, redirect, request # import flask modules for routes to work properly
from flask_app.models import ninja # import dojo model to connect to databse
from flask_app.models import dojo # import dojo model to connect to databse

@app.route('/ninjas') # load html for user to complete form with ninja data
def new_ninja():
    # get all dojos from dojos table to send to web page
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template('add_ninja.html', dojos = all_dojos)

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    #add new ninja to the ninjas table
    new_ninja_id = ninja.Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

@app.route('/ninjas/delete/<int:dojo_id>/<int:ninja_id>')
def delete_ninja(dojo_id, ninja_id):
    # initiate db query to remove row from table by provided ID
    ninja.Ninja.delete_ninja_by_id(ninja_id)
    return redirect(f"/dojos/{dojo_id}")

@app.route('/ninjas/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    all_dojos = dojo.Dojo.get_all_dojos()
    ninja_to_edit = ninja.Ninja.get_one_ninja(ninja_id)
    return render_template('edit_ninja.html', dojos = all_dojos, this_ninja = ninja_to_edit)

@app.route('/process_ninja_edit', methods=['POST'])
def process_edit():
    ninja.Ninja.update_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")