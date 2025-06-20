# app.py
from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os, sqlite3
from steganography import encode_image, decode_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists"
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        if 'cover_image' not in request.files:
            return "Error: No file part"
        cover = request.files['cover_image']
        if cover.filename == '':
            return "Error: No file selected"
        if cover.content_length and cover.content_length > 1 * 1024 * 1024:
            return "Image too large. Must be under 1MB."

        message = request.form.get('message')
        if not message:
            return "Error: Message is required"

        cover_path = os.path.join(UPLOAD_FOLDER, secure_filename(cover.filename))
        cover.save(cover_path)
        output_path = os.path.join(UPLOAD_FOLDER, 'encoded.png')
        encode_image(cover_path, message, output_path)
        return render_template('result.html', image=output_path)
    return render_template('encode.html')

@app.route('/download')
def download():
    path = os.path.join(UPLOAD_FOLDER, 'encoded.png')
    return send_file(path, as_attachment=True)

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        encoded = request.files['encoded_image']
        encoded_path = os.path.join(UPLOAD_FOLDER, secure_filename(encoded.filename))
        encoded.save(encoded_path)
        message = decode_image(encoded_path)
        return render_template('result.html', message=message)
    return render_template('decode.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)