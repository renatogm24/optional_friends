from flask import render_template, request, redirect

from flask_app.models import user
from flask_app.models import friendship

from flask_app import app

@app.route('/')
def index():
    users = user.User.get_all()
    friendships = friendship.Friendship.get_friendships()
    return render_template("index.html",users=users, friendships=friendships)

@app.route('/users/add_friendships',methods=['POST'])
def create():
    data = {
        "user_id":request.form['user_id'],
        "friend_id":request.form['friend_id'],
    }
    print(friendship.Friendship.exist_friendship(data))
    if not friendship.Friendship.exist_friendship(data):
      friendship.Friendship.save(data)
    return redirect('/')

@app.route('/users/add_user',methods=['POST'])
def createUser():
    data = {
        "first_name":request.form['first_name'],
        "last_name": "",
    }
    user.User.save(data)
    return redirect('/')