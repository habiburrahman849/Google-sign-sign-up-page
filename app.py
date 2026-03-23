from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
import sqlite3
import os
from datetime import datetime
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
bcrypt = Bcrypt(app)

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password_hash TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Validate email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Input validation
def validate_input(username, email, password):
    errors = []
    
    if len(username) < 3 or len(username) > 20:
        errors.append("Username must be between 3 and 20 characters.")
    
    if not is_valid_email(email):
        errors.append("Please enter a valid email address.")
        
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
        
    # Check for special characters in username
    if not re.match("^[a-zA-Z0-9_]+$", username):
        errors.append("Username can only contain letters, numbers, and underscores.")
    
    return errors

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']
        
        errors = validate_input(username, email, password)
        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('register'))
        
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                      (username, email, password_hash))
            conn.commit()
            conn.close()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists!', 'error')
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT id, username, password_hash FROM users WHERE username=? OR email=?", (username, username))
        user = c.fetchone()
        conn.close()
        
        if user and bcrypt.check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username, email, created_at FROM users WHERE id=?", (session['user_id'],))
    user_data = c.fetchone()
    conn.close()
    
    return render_template('dashboard.html', user=user_data)

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('welcome'))

# Welcome page (home)
@app.route('/')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)