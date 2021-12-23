from datetime import timedelta
import base64
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
app = Flask(__name__)

app.config["SECRET_KEY"] = base64.b64encode("Zhugedeptrai".encode())
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    return render_template('Home.html', current_year=2021)


@app.route('/user')
def user():
    if 'user' in session:
        name = session['user']
        return f"<h1 style='color: red'>Hello {name}! Welcome to Zhuge's Flask App!</h1>"
    return redirect(url_for('login'))


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usremail = request.form['email']
        password = request.form['password']
        session.permanent = True
        if usremail == 'admin':
            session['user'] = usremail
            flash(f"Welcome {usremail}")
            return redirect(url_for('admin'))
        else:
            session['user'] = usremail
            if password:
                return redirect(url_for('user', name=usremail))
    if 'user' in session:
        name = session['user']
        return f"<h1 style='color: red'>Hello {name}! Welcome to Zhuge's Flask App!</h1>"
    return render_template('login.html', current_year=2021)


@app.route('/logout')
def logout():
    if 'user' in session:
        name = session['user']
        flash(f"You have been logged out, {name}!", "info")

    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
