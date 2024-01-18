from flask import Blueprint,flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Post, User
from . import db
import json





views= Blueprint("views", __name__)

@views.route("/")
@views.route("/home", methods=['GET','POST'])
@login_required
def home():
    message=None

    if request.method=="GET":
        mesaje=Post.query.all()

    if request.method=="POST":
        message=request.form.get('message')
    if not message:
        flash('message is empty', category='erro')
    else:
        new_message= Post(text=message, author=current_user.id)
        db.session.add(new_message)
        db.session.commit()
        flash('mesaj trimis')


        return redirect(url_for('views.home'))







    return render_template("home.html" , user=current_user , mesaje=mesaje)


@views.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method=="GET":
        user=User.query.all() 
    return render_template("admin.html" , users=user)



@views.route("/delete_user" ,methods=['GET', 'POST'])
def delete_user():
  
    username=request.form.get("username")
    user_exists = User.query.filter_by(username=username).first()
    if user_exists:
        db.session.delete(user_exists)
        db.session.commit()
        return redirect(url_for("views.admin"))
    else:
        
        return "User not found"

        
@views.route("/change_user" ,methods=['GET','POST'])
def change_user():
    
    
    username=request.form.get("usernamechange")
    new_username=request.form.get("newusername")
    user_exists = User.query.filter_by(username=username).first()
    if user_exists:
        user_exists.username=new_username
        db.session.commit()
       
        return redirect(url_for("views.admin"))
    else:
        
        return "User not found"
    
    
@views.route("/sort")
def sort():
    
    users=User.query.all() 
    array=[]
    for user in users:
        array.append(user.username)
    array= sorted(array, reverse=True)
    array=json.dumps(array)
    return array

