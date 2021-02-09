from flask import Flask,render_template,request,redirect,url_for
import sqlite3
import hashlib

def validate(username,password):
    cond = False
    with sqlite3.connect('login.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        cond=check_password(dbPass, password)
    return cond

def check_password(hashed_psw,user_psw):
    return hashed_psw==user_psw

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST']) #http://127.0.0.1:5000/
def login():
    error=None
    if request.method == 'POST':
        username= request.form['uname']
        password= request.form['psw']
        completion = validate(username,password)
        if completion == False:
            error= 'Invalid Credential. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route("/secret/") #http://127.0.0.1:5000/pagina2
def secret():
    return "This is a secret page!"

if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True)
    