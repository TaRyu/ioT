from flask import render_template, redirect, url_for, make_response
from . import main


@main.route('/')
def index():
    light = 1
    return render_template('index.html', light=light)


@main.route('/turnon')
def turnon():
    print('1')
    return make_response(redirect(url_for('.index')))


@main.route('/turnoff')
def trunoff():
    print('2')
    return make_response(redirect(url_for('.index')))
