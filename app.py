from flask import Flask, render_template, Response,jsonify,request,session


from flask_wtf import FlaskForm


from wtforms import FileField, SubmitField,StringField,DecimalRangeField,IntegerRangeField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired,NumberRange
import os


import cv2
from YOLO_Video import video_detection
from video_temp import video_detection_vid
app = Flask(__name__)

app.config['SECRET_KEY'] = 'maskboy'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File",validators=[InputRequired()])
    submit = SubmitField("Run")


def generate_frames(path_x = ''):
    yolo_output = video_detection_vid(path_x)
    for detection_ in yolo_output:
        if detection_ is not None:
            ref,buffer=cv2.imencode('.jpg',detection_)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')

def generate_frames_web(receiver,path_x):
    yolo_output = video_detection(path_x,receiver)
    for detection_ in yolo_output:
        if detection_ is not None:
            ref,buffer=cv2.imencode('.jpg',detection_)

            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    session.clear()
    return render_template('index.html')
@app.route("/webcam", methods=['GET','POST'])
def webcam():
    session.clear()
    return render_template('ui.html')
@app.route('/FrontPage', methods=['GET','POST'])
def front():
    form = UploadFileForm()
    if form.validate_on_submit():
        # Our uploaded video file path is saved here
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))  # Then save the file
        # Use session storage to save video file path
        session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                                             secure_filename(file.filename))
    return render_template('videoprojectnew.html', form=form)
@app.route('/video')
def video():
    return Response(generate_frames(path_x = session.get('video_path', None)),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/webapp')
def webapp():
    email = request.args.get('email')
    print(email)
    return Response(generate_frames_web(email,path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/signup", methods=['GET','POST'])
def signup():
    session.clear()
    return render_template('signup.html')

@app.route("/profile", methods=['GET','POST'])
@app.route("/profile", methods=['GET','POST'])
def profile():
    session.clear()
    return render_template('home.html')
@app.route("/email",methods=['GET','POST'])
def email():
    email = request.form.get("email")
    # print(email)
    return email

if __name__ == "__main__":
    app.run(debug=True)