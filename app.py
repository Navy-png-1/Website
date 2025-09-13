from flask import Flask, render_template, request, url_for, send_from_directory
from datetime import date, time
import os

app = Flask(__name__)
posts = [{"id":"11", "date":"8/16/2025", "content":"Info", "name":"Personal Info", "title":"Don't Know"}, {"id":"12", "date":"9/13/2025", "content":"Information", "name":"Name", "title":"Title"}]

@app.route("/test")
def hello():
    return render_template("test.html")
@app.route("/journal")
def journal():
    return render_template("journal.html")
@app.route("/journal/posts")
def view_post():
    return render_template("posts.html", posts=posts)
@app.route("/journal/new", methods=['GET', 'POST'])
def new_post():
    #http://127.0.0.1:5000/journal/new?title=Title&name=Name&content=Content
    if request.method=='GET':
        title = request.form.get('title')
        name = request.form.get('name')
        content = request.form.get('content')
        id = len(posts) + 1
        date = time.strftime("%A %d. %B %Y")
    return render_template("new_posts.html")
@app.route("/form_submission")
def form_sub():
    return render_template("form.html")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)