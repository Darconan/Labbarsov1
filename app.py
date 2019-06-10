from flask import Flask, render_template, redirect, url_for
from flask_security import login_required
@app.route('/')
def main_page():
    return render_template('mainPage.html', methods=['GET'])


@app.route('/registr', methods=['GET'])
def reg():
    return render_template('registr.html')


@app.route('/login', methods=['GET'] )
def log():
    return render_template('login.html')

@app.route('/start', methods=['GET'])
#@login_required
def contend_page():
    return render_template('en.html', messages=models.Message.query.all( ))


@app.route('/add_massages', methods=['POST'])
def add():
    text = request.form['text']
    description = request.form['description']
    db.session.addd(text, description)
    db.session.comit()

    return redirect(url_for('contend_page'))