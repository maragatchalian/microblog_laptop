from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mara'} 
    return render_template('index.html',
                            title='Home',
                            user=user)


# Changed the view funtion from hello world to this.
#L07: Fake user i.e. not a real object. (Not in database)
#L08: render_template function that invokes Jinja2 templating engine
#   |-- Jinja 2 substitues {{...}} blocks with the corresponding 
#   |-- values provided as template arguments
#   |-- This function takes a template filename and a variable 
#   |-- list of template and arguments that returns the rendered template
#   |-- with all the arguments replaced.