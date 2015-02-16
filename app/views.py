from app import app

from flask import render_template, redirect, url_for

from .forms import Usuario
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title = 'Home - Academia')

@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    form = Usuario()
    if form.validate_on_submit():
        return redirect('/home')

    return render_template('cadastro.html', form = form)
