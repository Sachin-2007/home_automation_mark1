from flask import Flask, request, render_template, redirect, url_for, Response
from controls import *
from cctv import gen_frames
import RPi.GPIO as gpio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/redirect', methods=['GET', 'POST'])
def redirect_page():
    code = str(request.form['coode'])
    if code == 'control':
        return redirect(url_for('control'))
    elif code == 'cctv':
        return redirect(url_for('cctv'))

@app.route('/control', methods=['GET', 'POST'])
def control():
    return render_template('control.html')

@app.route('/cctv', methods=['GET', 'POST'])
def cctv():
    return render_template('cctv.html')

@app.route("/on", methods=['GET', 'POST'])
def on():
    light_on()
    print('ON')
    return ('', 204)

@app.route("/off", methods=['GET', 'POST'])
def off():
    light_off()
    print('OFF')
    return ('', 204)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)
except KeyboardInterrupt:
    gpio.cleanup()
    print('clean')
finally:
    gpio.cleanup()
    print('clean')
