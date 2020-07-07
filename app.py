from flask import Flask, render_template, url_for, flash, redirect,request,session,logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


from passlib.hash import sha256_crypt




app = Flask(__name__)



app.config['SECRET_KEY'] ='hbgoyivouyvoutcf6yguyv5uygut5tviyt'


all_reminders = [
    {
        'author': 'meeting with mouhmed',
        'title': 'remind 1',
        'content': 'this is the first remind'
        
               
    },
    {
        'author': 'reunion with school',
        'title': 'remind 2',
        'content': 'this is the second remind'
               
    },
    {
        'author': 'appointment with dentist',
        'title': 'remind 3',
        'content': 'this is the third remind'
    },
    {
        'author': 'appointment with head master',
        'title': 'remind 4',
        'content': 'this is the third remind'
    }
]

    
@app.route("/reminders")
def reminders():
    return render_template('reminders.html', reminders=all_reminders)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/register",methods=["GET","POST"])
def register():
    return render_template('register.html', title='Register')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')


if __name__ == '__main__':
    app.run(debug=True)
