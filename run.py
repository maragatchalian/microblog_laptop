#!flask/bin/python
from app import app
app.run(debug=True)

#L02: Import 'app' variable from 'app' package
#  |--app variable holds the flask instance that was created in __init__.py