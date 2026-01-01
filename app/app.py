from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the srinivas 's Cap stone project"

@app.route("/srinu")
def srinu():
    return "Thanks for Visiting !!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
