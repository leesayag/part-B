from flask import Flask, request, session
import flask

app = Flask(__name__, static_url_path='', static_folder='static',
            template_folder='static/templates')

app.secret_key = "test"

users = [
    {"name": "Yossi", "email": "yossi@gmail.com"},
    {"name": "Amir", "email": "amir@gmail.com"},
    {"name": "Guy", "email": "guy@gmail.com"},
    {"name": "Gal", "email": "gal@gmail.com"},
    {"name": "Assaf", "email": "assaf@gmail.com"},
]


@ app.route('/')
def home():
    return flask.render_template('home.html', userLoggedIn=session.get('userLoggedIn'))


@ app.route('/contact')
def contact():
    return flask.render_template('contact.html', userLoggedIn=session.get('userLoggedIn'))


@ app.route('/assignment3_1')
def assignment3_1():
    return flask.render_template('assignment3_1.html', userLoggedIn=session.get('userLoggedIn'))


@ app.route('/logout')
def logout():
    session['userLoggedIn'] = None
    search = {'name': '', 'email': ''}
    return flask.render_template('assignment3_2.html', search=search, len=len(users), users=users, userLoggedIn=session.get('userLoggedIn'))


@ app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    # GET
    args = request.args
    usersToReturn = []
    search = {'name': '', 'email': ''}
    if('name' in args and args['name'] != ''):
        search['name'] = args['name']

    if('email' in args and args['email'] != ''):
        search['email'] = args['email']

    for user in users:
        if((search['name'] != '' and search['name'] in str(user['name'])) or (search['email'] != '' and search['email'] in str(user['email']))):
            usersToReturn.append(user)
        if(search['name'] == '' and search['email'] == ''):
            usersToReturn.append(user)

    # POST
    if (request.values.get('nickname')):
        session['userLoggedIn'] = request.values.get('nickname')

    return flask.render_template('assignment3_2.html', search=search, len=len(usersToReturn), users=usersToReturn, userLoggedIn=session.get('userLoggedIn'))


@ app.route('/redirect')
def redirect():
    return flask.redirect('/')
