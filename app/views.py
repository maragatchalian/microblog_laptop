from flask import render_template
from app import app

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

# L07: Fake user.
# L08 - L19 : Fake array of posts.
