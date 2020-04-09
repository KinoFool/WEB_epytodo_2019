from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from forms import SignUpForm

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
        return render_template("register.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
        form = SignUpForm()
        if form.is_submitted():
                result = request.form
                return render_template("yes.html", result=result)
        return render_template("signin.html", form=form)