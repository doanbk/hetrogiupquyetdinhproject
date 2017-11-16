from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from schoolsql import select_school, insert_school, update_file
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def do_admin_login():
    school= select_school(request.form['username'])
    if request.form['password'] == school.getPassword():
        session['logged_in'] = True
    else:
        session['logged_in'] = False
        flash('wrong password!')
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)


