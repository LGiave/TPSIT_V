from flask import Flask,render_template,request,redirect,url_for
import AlphaBot
import time
t=AlphaBot.AlphaBot()
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])       
def index():                
    if request.method == 'POST':
        direction=request.form['avanti']
        stop=request.form['finish']
        if direction=='avanti':
            t.forward()
            time.sleep(3)
            t.stop()
            #return 'avanti'
        if direction=='indietro':
            t.backward()
            time.sleep(3)
            t.stop()
            #return 'indietro'
        if direction=='destra':
            t.right()
            time.sleep(3)
            t.stop()
            #return 'destra'
        if direction=='sinistra':
            t.left()
            time.sleep(3)
            t.stop()
            #return 'sinistra'
        if stop==1:
            return redirect('secret.html')
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug = True)