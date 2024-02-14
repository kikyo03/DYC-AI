# from flask import Flask, render_template, request, jsonify, session, redirect, url_for
# from flask_cors import CORS
# from chat import get_response
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re

# app = Flask(__name__)
# CORS(app)

# @app.post("/predict") 
# def predict():
#     text = request.get_json().get("message")	
#     # todo if chat is valid
#     response = get_response(text)
#     message = {"answer":response}
#     return jsonify(message)

# app.secret_key = 'xyzsdfg'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'login-flask'
  
# mysql = MySQL(app)

# @app.route('/')
# @app.route('/login', methods =['GET', 'POST'])
# def login():
#     mesage = ''
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
#         user = cursor.fetchone()
#         if user:
#             session['loggedin'] = True
#             session['name'] = user['name']
#             session['email'] = user['email']
#             mesage = 'Logged in successfully !'
#             return render_template('index.html', mesage = mesage) #main chatbot
#         else:
#             mesage = 'Please enter correct email / password !'
#     return render_template('login.html', mesage = mesage)


# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('email', None)
#     return redirect(url_for('login'))

# # end
  
# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     mesage = ''
#     if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
#         userName = request.form['name']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
#         account = cursor.fetchone()
#         if account:
#             mesage = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             mesage = 'Invalid email address !'
#         elif not userName or not password or not email:
#             mesage = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO user VALUES (% s, % s, % s)', (userName, email, password, ))
#             mysql.connection.commit()
#             mesage = 'You have successfully registered !'
#     elif request.method == 'POST':
#         mesage = 'Please fill out the form !'
#     return render_template('register.html', mesage = mesage)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
from chat import get_response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
CORS(app)

@app.post("/predict") 
def predict():
    text = request.get_json().get("message")	
    # todo if chat is valid
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login-flask'
  
mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('index.html', mesage = mesage) #main chatbot
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)


@app.route('/logout', methods=['POST'])
def logout():
    if request.form.get('confirm') == 'yes':
        session.pop('loggedin', None)
        session.pop('email', None)
    return redirect(url_for('login'))

# end
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (% s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

if __name__ == "__main__":
    app.run(debug=True)
