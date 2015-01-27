# coding: utf-8
import os
import glob
import time
from app import create_app
from flask.ext.script import Manager, Shell
import RPi.GPIO as GPIO

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
light = 0
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def readTempRaw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def readTemp():
    lines = readTempRaw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempRaw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return round(temp_c, 1)


def make_shell_context():
    return dict(app=app)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    while True:
        temp = readTemp()
        time.sleep(5)
