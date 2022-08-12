import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

def light_on():
    gpio.output(18, 1)
    return '1'

def light_off():
    gpio.output(18, 0)
    return '1'
