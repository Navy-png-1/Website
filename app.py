from flask import Flask, render_template, request, url_for, send_from_directory
from datetime import date, time, datetime
import os

app = Flask(__name__)
posts = [{}]
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
    if request.method=='POST':
        title = request.form.get('title')
        name = request.form.get('name')
        content = request.form.get('content')
        id = len(posts) + 1
        date = datetime.now().strftime("%A %d. %B %Y")
        file = request.files.get('file')
        filename = file.filename
        file.save("uploads/"+filename)
        posts.append({"id": id, "date":date,"content":content,"name": name, "title":title, "file":file})
    return render_template("new_posts.html")
@app.route("/form_submission")
def form_sub():
    return render_template("form.html")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)