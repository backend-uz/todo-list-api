from todo import app


@app.route('/')
def index():
    return '<h1>app is working now!</h1>'