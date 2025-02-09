from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# SQLite database setup
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Login page with SQLi vulnerability
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        # Vulnerable SQL query
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        if user:
            return "Login successful!"
        else:
            return "Login failed!"
    return render_template('login.html')

# Command injection page
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        host = request.form['host']
        # Vulnerable command execution
        result = os.popen(f"ping -c 4 {host}").read()
        return f"<pre>{result}</pre>"
    return render_template('ping.html')

# XSS page
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment = request.form['comment']
        return f"Your comment: {comment}"
    return render_template('comment.html')

# CSRF page
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        # Simulate password change
        return f"Password changed to: {new_password}"
    return render_template('change_password.html')

if __name__ == '__main__':
    app.run(debug=True)
