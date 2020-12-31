from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Manos'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {   'author': {'username': 'Manos'},
            'body': 'Greetings from Athens!'
        }
    ]

    return render_template('index.html', title='Das Home', user=user, posts=posts)