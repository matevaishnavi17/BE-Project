from flask import Flask, render_template, Response, request
import cv2
from detector import detection

app = Flask(__name__)

camera = cv2.VideoCapture(0)  


def gen_frames():
    while(True):
        success,frame = camera.read()
        if not success:
            print("Alert ! Camera disconnected")
        else:
            detected = detection(success, frame)
            ret, buffer = cv2.imencode('.jpg', detected)
            detected = buffer.tobytes()

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + detected + b'\r\n')




"""def gen_text():
    while(True):
        success,frame = camera.read()
        if not success:
            print("Alert ! Camera disconnected")
        else:
            detected = detection(success, frame)
            y_pred = "0"
            text = letter(y_pred)
            print(y_pred)
            ret, buffer = cv2.imencode('.jpg',detected)
            detected = buffer.tobytes()
        yield text"""





 

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')


"""@app.route('/text', methods =["GET", "POST"])
def text():
    return Response(gen_text(), mimetype='multipart/x-mixed-replaces; boundary=frame')"""



if __name__ == '__main__':
    app.run(debug=True)