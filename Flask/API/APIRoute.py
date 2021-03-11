from flask import Flask,url_for,jsonify,request
import flask,sqlite3
start=[]
end=[]

with sqlite3.connect('route.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    start.append(row[0])
                    end.append(row[1])

app= flask.Flask(__name__)
app.config["DEBUG"]= True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Percorso Alphabot</>"

@app.route('/route',methods=['GET'])
def api_all():

    print(jsonify(start,end))
    return jsonify(start,end)