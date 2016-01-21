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
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign-in',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

# L07: Fake user.
# L08 - L19 : Fake array of posts.
# L24: 
#   |--This tells Flask that this view function accepts GET and POST requests.
#   |--Without this the view will only accept GET requests.
#   |--We will want to receive the POST requests, these are the ones that will 
#   |--bring in the form data entered by the user.
# L27: validate_on_submit
#   |-- will gather all the data, run all the validators attached to fields, 
#   |--and if everything is all right it will return True
# L28: flash
#   |-- quick way to show a message regarding the user's action 
#   |-- We will add these messages to the base template, so that all our templates inherit this functionality. 