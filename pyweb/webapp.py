from weiapp import weiapp
from mycgi import mycgi


app = weiapp()

@app.route('/')
def index():
    return 'hello index'

@app.route('/about')
def about():
    return 'about'


server = mycgi(app=app)
server.start()