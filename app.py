# save this as app.py
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/home")
def hello():
    return render_template("file3.html")
    #return "Hello, World!"
@app.route("/form_submission")
def form_sub():
    return render_template("File1.html")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)