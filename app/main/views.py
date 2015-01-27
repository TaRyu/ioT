from flask import render_template, url_for
from . import main
import RPi.GPIO as GPIO
import manage


@main.route('/')
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    return render_template('index.html', light=manage.light, temp=manage.temp)


@main.route('/turnon')
def turnon():
    manage.light = 1
    GPIO.output(25, GPIO.HIGH)
    return render_template('index.html', light=manage.light, temp=manage.temp)


@main.route('/turnoff')
def trunoff():
    manage.light = 0
    GPIO.output(25, GPIO.LOW)
    return render_template('index.html', light=manage.light, temp=manage.temp)
