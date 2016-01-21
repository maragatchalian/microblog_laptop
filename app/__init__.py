from flask import Flask 

app = Flask (__name__) 
app.config.from_object('config')

from app import views 

# L01: Creates the application object of flask 
# L03: App variable gets assigned to flask instance.
# L04: Tells flask to read and use the config.py
# L06: Imports the 'views' module. 
#   |-- This is the end, to avoid circular import error.
#   |-- The 'views' module needs to import the 'app' variable defined in this script.