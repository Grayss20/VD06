from flask import render_template, request, redirect, url_for
from app import app


posts = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post = {
            'title': request.form['title'],
            'content': request.form['content']
        }
        posts.append(post)
        return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)