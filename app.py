from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Puppy</h1"


@app.route("/information")
def info():
    return "<h1>Puppies are cute.</h1>"


@app.route("/puppy/<name>")
def puppy(name):
    return f"<h1>This is a page for {name.upper()}</h1>)"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return f"<h1>Your Puppy Latin Name is {pupname}"


if __name__ == "__main__":
    app.run(debug=True)
