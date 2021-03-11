from flask import Flask, render_template, Response
import cv2

app = Flask(_name_)
camera = cv2.VideoCapture(0)

def generator_frames():  
    while True:
        success, frame = camera.read()  
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            byteframe = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + byteframe + b'\r\n')  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generator_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if _name_ == "_main_":
    app.run(debug=True)