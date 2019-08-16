from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login')
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)
