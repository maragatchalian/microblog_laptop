from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

# Views are handlers that respond to requests from web browsers
# |--or other clients. 
# |--Each view function is mapped to one or more request URLs.

#L03 - L04 : 'route' decorators. Create mappings from URLs to this function.