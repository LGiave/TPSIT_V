import semaforo
from flask import Flask,render_template,request,redirect,url_for
import time, sqlite3 
from datetime import datetime 

app = Flask(__name__)

verde=2
rosso=2
giallo=1
on=1

s = semaforo.semaforo()
STATO = "ATTIVO" #"SPENTO"

def saveChanges(time,action):
    with sqlite3.connect('semaforo.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO acceso(x) data (y)", [(action),(time)])
    return 0

#ESEMPIO di pagina di test
@app.route('/semaforo')
def conf():
    if request.method == ['GET','POST']:
        verde= request.form['verde']
        giallo= request.form['giallo']
        rosso= request.form['rosso']
        on=request.form['on']

        if on=="1":
            STATO="spento"
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            saveChanges(STATO,current_time)
        else:
            STATO="ATTIVO"
        return "semaforo spento"
        
    return render_template("/semaforo.html")

@app.route('/')
def test():
    if STATO == "ATTIVO":
            #Esempio di sequenza con semaforo attivo. I tempi devono essere
            #modificabili dalla pagina di configurazione!
            s.rosso(rosso)
            s.verde(verde)
            s.giallo(giallo) 
            """
        if STATO == "ATTIVO":
            s.rosso(2)
            s.verde(2)
            s.giallo(1)
            """
    else:
        #Esempio di sequenza con semaforo spento. I tempi devono essere
        #modificabili dalla pagina di configurazione!
        for _ in range(3):
            s.giallo(1)
            s.luci_spente(1)

    return "test eseguito"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
