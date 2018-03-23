from flask import Flask

app = Flask(__name__)


# @ signifies a decorator - for wrapping function and modifying it's behavior
# @ map a url to a return value
@app.route('/')
def index():
    return 'Landing page'


@app.route('/home')
def home():
    return '<h1> Home Page </h1>'


@app.route('/data/<source>')
def data(source):
    return "Requesting <i> %s </i> data" % source


@app.route('/number/<int:num>')
def number(num):
    return "Number is %s " % num


# make sure to start the web server whenever this file is called directly
if __name__ == "__main__":
    app.run(debug=True)
