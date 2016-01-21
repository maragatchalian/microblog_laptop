from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mara'} 
    posts = [
        {
            'author': {'nickname': 'Eric'},
            'body': 'Beautiful Day in NYC!'
        },
        {
            'author': {'nickname': 'JJ'},
            'body': 'I like Tomica cars!'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title='Sign-in',
                            form=form)

# L07: Fake user.
# L08 - L19 : Fake array of posts.
# L24: 
#   |--This tells Flask that this view function accepts GET and POST requests.
#   |--Without this the view will only accept GET requests.
#   |--We will want to receive the POST requests, these are the ones that will 
#   |--bring in the form data entered by the user.