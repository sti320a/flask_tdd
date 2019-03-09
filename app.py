import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify


# Configuration
DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = 'my_test'
USERNAME = 'admin'
PASSWORD = 'admin'


# create and initialize app
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
         g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__=='__main__':
    init_db()
    app.run()

