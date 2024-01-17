from flask import Blueprint, render_template, redirect, url_for, request

auth= Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    return render_template("Sign in.html")

@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("pass")
    
    return render_template("Sign up.html")

@auth.route("/logout")
def logout():
    return "logout"