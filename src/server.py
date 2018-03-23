from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, lalal!'


@app.route('/home')
def home():
    return "This is home! "


if __name__ == "__main__":
    app.run(debug=True)
