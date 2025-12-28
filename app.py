from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import os, sqlite3
from steganography import encode_image, decode_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this_in_production'
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT UNIQUE, 
                  password TEXT)''')
    conn.commit()
    conn.close()

init_db()
@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
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
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials!', 'error')
        return render_template('login.html')
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
            flash('Registration successful! Please login.', 'success')
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!', 'error')
            conn.close()
            return render_template('register.html')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login to continue', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if 'user' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'cover_image' not in request.files:
            flash('No image selected!', 'error')
            return render_template('encode.html')
        
        cover = request.files['cover_image']
        if cover.filename == '':
            flash('Please select an image!', 'error')
            return render_template('encode.html')
        
        if cover.content_length and cover.content_length > 1 * 1024 * 1024:
            flash('Image too large! Must be under 1MB.', 'error')
            return render_template('encode.html')

        message = request.form.get('message')
        if not message or message.strip() == '':
            flash('Message cannot be empty!', 'error')
            return render_template('encode.html')

        try:
            cover_path = os.path.join(UPLOAD_FOLDER, secure_filename(cover.filename))
            cover.save(cover_path)
            output_path = os.path.join(UPLOAD_FOLDER, f'encoded_{session["user"]}.png')
            encode_image(cover_path, message, output_path)
            return render_template('result.html', image=output_path)
        except Exception as e:
            flash(f'Encoding failed: {str(e)}', 'error')
            return render_template('encode.html')
    
    return render_template('encode.html')

@app.route('/download')
def download():
    if 'user' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    path = os.path.join(UPLOAD_FOLDER, f'encoded_{session["user"]}.png')
    if os.path.exists(path):
        return send_file(path, as_attachment=True, download_name='encoded_image.png')
    flash('No encoded image found!', 'error')
    return redirect(url_for('dashboard'))

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if 'user' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'encoded_image' not in request.files:
            flash('No image selected!', 'error')
            return render_template('decode.html')
        
        encoded = request.files['encoded_image']
        if encoded.filename == '':
            flash('Please select an image!', 'error')
            return render_template('decode.html')
        
        try:
            encoded_path = os.path.join(UPLOAD_FOLDER, secure_filename(encoded.filename))
            encoded.save(encoded_path)
            message = decode_image(encoded_path)
            return render_template('result.html', message=message)
        except Exception as e:
            flash(f'Decoding failed: {str(e)}', 'error')
            return render_template('decode.html')
    
    return render_template('decode.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
