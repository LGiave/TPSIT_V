from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST']) #http://127.0.0.1:5000/
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cond = validate(username, password)
        print (username)
        if cond == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('accesso_eseguito'))
    return render_template('login.html', error=error)

def validate(username, password):
    cond = False
    with sqlite3.connect('static/db.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        cond=check_password(dbPass, password)
    return cond

def check_password(hashed_password, user_password):
    return hashed_password == user_password    

@app.route('/accesso_eseguito')
def accesso_eseguito():
    return "LOGIN EFFETTUATO"

if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True)