import json
import requests
import random
from flask import Flask, redirect, url_for, request, Blueprint, jsonify
from flask import render_template, session
import asyncio
import aiohttp
from pages.assignment4.assignment4 import assignment4
from interact_with_DB import interact_db
app = Flask(__name__)
app.register_blueprint(assignment4)
app.secret_key = '123'


@app.route('/')
def cv_main_page():
    return render_template('base.html')

@app.route('/header')
def header_page():
    return render_template('header.html')


users = {
  'yossi':{"name": "Yossi", "email": "yossi@gmail.com"},
    'amir':{"name": "Amir", "email": "amir@gmail.com"},
    'guy':{"name": "Guy", "email": "guy@gmail.com"},
   'gal': {"name": "Gal", "email": "gal@gmail.com"},
    'assaf':{"name": "Assaf", "email": "assaf@gmail.com"},
}



@app.route('/assignment4/outer_source')
def outer_source():
    return render_template('Back-Front.html')







@app.route('/assignment4/users')
def assignment4_userJson():
    query = 'select  id,name,email from users;'
    users = interact_db(query=query, query_type='fetch')
    response = []
    for user in users:
        response.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })
    return render_template('users.html', users=json.dumps(response))

@app.route('/assignment4/outer_source/json')
def assignment4_def_json():
    number = request.args['number']
    res = requests.get("https://reqres.in/api/users/{}".format(number))
    response = jsonify(res.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/assignment4/restapi/', defaults={'user_id':60})
@app.route('/assignment4/restapi/<int:user_id>')
def get_users_def(user_id):
    query = 'select  id,name,email from users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0 :
        user_dict = {
            'status' : 'failed' ,
            'message' : 'user not found'
        }
    else:
        user_dict = {
            'status': 'success',
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email
        }
    return jsonify(user_dict)




if __name__ == '__main__':
    app.run(debug=True)




