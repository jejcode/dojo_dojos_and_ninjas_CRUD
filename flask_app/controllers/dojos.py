from flask_app import app # import app to manage routes
from flask import render_template, redirect, request # import flask modules for routes to work properly
from flask_app.models import dojo # import dojo model to connect to databse
from flask_app.models import ninja # import ninja model to connect to databse

# routes
@app.route('/')
def default():
    return redirect('/dojos')
@app.route('/dojos')
def dojos():
    # get all dojos from database
    all_dojos = dojo.Dojo.get_all_dojos() # returns list of db rows
    return render_template('dojos.html', dojos = all_dojos) # pass db rows to html

@app.route('/add_dojo', methods=['POST']) # adds dojo record to dojos table
def add_dojo():
    dojo.Dojo.create_dojo(request.form) # returns id of newly created row
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    #get joined databse grouped by dojo id
    result = ninja.Ninja.get_all_ninjas_in_one_dojo(dojo_id)
    return render_template('show_one_dojo.html', this_dojo = result)