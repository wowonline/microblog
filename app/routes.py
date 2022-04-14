from app import app

@app.route('/jopa')
@app.route('/')
@app.route('/index')
def index():
    return 'Hello world!'