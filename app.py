from flask import Flask, request, render_template
import RPi.GPIO as gpio
import controls

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/on", methods=['GET', 'POST'])
def on():
    controls.light_on()
	print('ON')
	return ('', 204)

@app.route("/off", methods=['GET', 'POST'])
def off():
    controls.light_off()
    print('OFF')
    return ('', 204)

try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)
except KeyboardInterrupt:
    gpio.cleanup()
finally:
    gpio.cleanup()
