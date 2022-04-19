from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Egor'}
    posts = [
        {
            'author': {'username': 'Chmoshnik'},
            'body': 'Ya uchus` na vmike! I eto kruto'
        },
        {
            'author': {'username': 'Nikita'},
            'body': 'Ya takoy koncheniy!'
        },
        {
            'author': {'username': 'Yarik'},
            'body': 'Nado vcativat`sya v rast!!!!'
        }
    ]
    return render_template('index.html', title='title_name', user=user, 
                           posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login title', form=form)