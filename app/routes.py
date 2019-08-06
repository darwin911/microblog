from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'HAL 9000'}
    posts = [
      {
        'author': {'username': 'Robert'},
        'body': 'Python and Flask are the bomb.'
      },
      {
        'author': {'username': 'Dan'},
        'body': 'What is Python? Redux is better.'
      }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
