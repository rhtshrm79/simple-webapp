from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, welcome to my app"

app.run(debug=True)

