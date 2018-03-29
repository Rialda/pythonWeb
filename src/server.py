from flask import Flask, render_template

app = Flask(__name__)


# @ signifies a decorator - for wrapping function and modifying it's behavior
# @ map a url to a return value
@app.route('/')
def index():
    return 'Index'


@app.route('/data/<soc_media>')
def data(soc_media):
    return 'Data: %s' % soc_media


# make sure to start the web server whenever this file is called directly
if __name__ == "__main__":
    app.run(debug=True)


