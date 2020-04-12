from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection
from .register import add_user
from .signin import check_user
from .task import create_task
from .task import get_task
from app import user_id

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    global user_id
    if request.method == 'POST':
        user_id = add_user((request.form['username']), request.form['password'])
        if user_id != 0:
            return redirect('/task')
    return render_template("register.html")

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    global user_id
    if request.method == 'POST':
        id = check_user(request.form['username'], request.form['password'])
        user_id = id[0]
        if user_id != None:
            print("L ============================>", user_id)
            return redirect('/task')
    return render_template("signin.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
        return render_template("contact.html")

@app.route('/task/', methods=['GET', 'POST'])
def todo():
    print("USER ID ==>", user_id)
    if request.method == 'POST':
        create_task(user_id, request.form['title'], request.form['begin'], request.form['end'])
    return render_template("todo.html", usertasks=get_task(user_id), lenght=len(get_task(user_id)))

@app.route('/user', methods=['GET', 'POST'])
def user():
        return render_template("user.html")
