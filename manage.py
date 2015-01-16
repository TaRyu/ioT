# coding: utf-8
#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager, Shell
import RPi.GPIO as GPIO

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
light = 0


def make_shell_context():
    return dict(app=app)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
