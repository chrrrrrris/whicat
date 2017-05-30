import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


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


class UrlForm(Form):
    url = StringField('URL:', validators=[validators.required()])


def reduceURL(url):
    if(url[4] == 's'):
        return url[8:]
    else:
        return url[7:]



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


@app.route('/checklist', methods=['GET', 'POST'])
def enterUrl():
    form = UrlForm()
    if request.method == 'POST':
        name = request.form['URL']
        print name
        session['name'] = name
        return redirect(url_for('question1'))
    return render_template('checklist.html',
                           form=form)


@app.route('/checklist/question/1', methods=['GET', 'POST'])
def question1():
    name = session['name']
    print "q1"
    print name
    return render_template('checklist-Q1.html', name=name, title=reduceURL(name))

@app.route('/checklist/question/2', methods=['GET', 'POST'])
def question2():
    name = session['name']
    return render_template('checklist-Q2.html', name=name)


@app.route('/checklist/question/3', methods=['GET', 'POST'])
def question3():
    name = session['name']
    return render_template('checklist-Q3.html', name=name)


@app.route('/checklist/question/4', methods=['GET', 'POST'])
def question4():
    name = session['name']
    return render_template('checklist-Q4.html', name=name)


@app.route('/checklist/question/5', methods=['GET', 'POST'])
def question5():
    name = session['name']
    return render_template('checklist-Q5.html', name=name)


@app.route('/checklist/question/6', methods=['GET', 'POST'])
def question6():
    name = session['name']
    return render_template('checklist-Q6.html', name=name)


@app.route('/checklist/question/7', methods=['GET', 'POST'])
def question7():
    name = session['name']
    return render_template('checklist-Q7.html', name=name)


@app.route('/checklist/question/8', methods=['GET', 'POST'])
def question8():
    name = session['name']
    return render_template('checklist-Q8.html', name=name)


@app.route('/checklist/question/9', methods=['GET', 'POST'])
def question9():
    name = session['name']
    return render_template('checklist-Q9.html', name=name)


@app.route('/checklist/question/10', methods=['GET', 'POST'])
def question10():
    name = session['name']
    return render_template('checklist-Q10.html', name=name)


@app.route('/checklist/question/11', methods=['GET', 'POST'])
def question11():
    name = session['name']
    return render_template('checklist-Q11.html', name=name)


@app.route('/checklist/question/12', methods=['GET', 'POST'])
def question12():
    name = session['name']
    return render_template('checklist-Q12.html', name=name)

@app.route('/checklist/end', methods=['GET', 'POST'])
def end():
    return render_template('checklist-end.html')


if __name__ == '__main__':
    app.run()