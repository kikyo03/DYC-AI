from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
from flask import session
import mysql.connector
from chat import get_response
import re
import json

app = Flask(__name__)
CORS(app)

# Load responses from JSON file
with open('intents.json', 'r') as file:
    responses = json.load(file)




app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login-flask'

try:
    mysql = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        port=3306,  # Change the port number to your MySQL server port if it's different
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    print("Connected to MySQL database")
except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = session['message'] = 'You have successfully registered!'
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully!'
            return render_template('index.html', message=message)  # main chatbot
        else:
            message = 'Please enter correct email / password!'
        cursor.close()
    return render_template('login.html', message=message)

@app.post("/predict") 
def predict():
    text = request.get_json().get("message")	
    # todo if chat is valid
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

@app.route('/logout', methods=['POST'])
def logout():
    if request.form.get('confirm') == 'yes':
        session.pop('loggedin', None)
        session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not userName or not password or not email:
            message = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO user (name, email, password) VALUES (%s, %s, %s)', (userName, email, password,))
            mysql.commit()
            session['message'] = 'You have successfully registered!'
            return redirect(url_for('login'))
        cursor.close()
    elif request.method == 'POST':
        message = 'Please fill out the form!'
    return render_template('register.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
