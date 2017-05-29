import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , app.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'whicat.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialised the database.')

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    #checked = request.form.getlist('Q1')
    checked=request.form['Q1']
    with open('checked.txt','w') as file:
        file.write("%s"%checked)
    # do something with checked array
    return checked

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/checklist')
def checklist():
    return render_template('checklist.html')


@app.route('/checklist/question/1', methods=['GET', 'POST'])
def question1():
    return render_template('checklist-Q1.html')

@app.route('/checklist/question/2', methods=['GET', 'POST'])
def question2():
    return render_template('checklist-Q2.html')


@app.route('/checklist/question/3', methods=['GET', 'POST'])
def question3():
    return render_template('checklist-Q3.html')


@app.route('/checklist/question/4', methods=['GET', 'POST'])
def question4():
    return render_template('checklist-Q4.html')


@app.route('/checklist/question/12', methods=['GET', 'POST'])
def question12():
    return render_template('checklist-Q12.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')