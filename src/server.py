from flask import Flask, request

app = Flask(__name__)


# @ signifies a decorator - for wrapping function and modifying it's behavior
# @ map a url to a return value
@app.route('/')
def index():
    return 'Method used: %s ' % request.method


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"


# make sure to start the web server whenever this file is called directly
if __name__ == "__main__":
    app.run(debug=True)
