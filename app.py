# importing flask
from flask import Flask

# init app & constructor
app = Flask(__name__)

# rendering (URL)
@app.route('/')
def hello():
    return "Hello, Flask!"

# rendering (URL)
@app.route('/hello/<name>')
def check(name):
    return "Hello, %s!" % name


# main function
if __name__ == '__main__':
    app.run(debug = True)
