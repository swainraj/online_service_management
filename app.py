from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.before_first_request
def create_admin():
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM users WHERE role='admin'")
    admin = cursor.fetchone()
    if not admin:
        cursor.execute("INSERT INTO users (username, password, mobile_number, role) VALUES (%s, %s, %s, %s)", ('admin', 'admin_password', '0000000000', 'admin'))
        mysql.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            if account['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif account['role'] == 'serviceman':
                return redirect(url_for('serviceman_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'mobile_number' in request.form:
        username = request.form['username']
        password = request.form['password']
        mobile_number = request.form['mobile_number']
        cursor = mysql.cursor()
        cursor.execute('INSERT INTO users (username, password, mobile_number, role) VALUES (%s, %s, %s, %s)', (username, password, mobile_number, 'user'))
        mysql.commit()
        msg = 'You have successfully registered!'
    return render_template('register.html', msg=msg)

@app.route('/user_dashboard')
def user_dashboard():
    if 'loggedin' in session:
        return 'User Dashboard: Logged in as ' + session['username'] + '<br><a href="/logout">Logout</a>'
    return redirect(url_for('login'))

@app.route('/serviceman_dashboard')
def serviceman_dashboard():
    if 'loggedin' in session:
        return 'Serviceman Dashboard: Logged in as ' + session['username'] + '<br><a href="/logout">Logout</a>'
    return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'loggedin' in session:
        return 'Admin Dashboard: Logged in as ' + session['username'] + '<br><a href="/logout">Logout</a>'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
