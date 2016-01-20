from flask import Flask 
app = Flask (__name__) 
from app import views 

# L01: Creates the application object of flask 
# L02: App variable gets assigned to flask instance.
# L03: Imports the 'views' module. 
#   |-- This is the end, to avoid circular import error.
#   |-- The 'views' module needs to import the 'app' variable defined in this script.