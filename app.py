# save this as app.py
from flask import Flask, render_template


app = Flask(__name__)
posts = [{"id":"11", "date":"8/16/2025", "content":"Info", "name":"Personal Info", "title":"Don't Know"}]
@app.route("/home")
def hello():
    return render_template("file3.html")
@app.route("/journal")
def journal():
    return render_template("file4.html")
@app.route("/journal/posts")
def posts():
    return render_template("posts.html", posts=posts)
@app.route("/form_submission")
def form_sub():
    return render_template("File1.html")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)