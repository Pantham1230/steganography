# 🕵️‍♀️ Image Steganography Web Application

## 📌 Project Overview
This project is a **web-based Image Steganography application** that allows users to **securely hide and retrieve secret messages inside a cover image**.  
The main goal is to demonstrate **secure data hiding techniques** using steganography while maintaining the visual quality of the image.

The application provides a simple and user-friendly interface to:
- Encode secret data into an image
- Decode hidden data from a stego image

## 🎯 Features
- 🔐 Secure message hiding using image steganography
- 🖼️ Encode secret text or image inside a cover image
- 🔍 Decode hidden data from stego image
- 👤 Login-based access for users
- 🌐 Web-based interface
- 📁 Supports multiple image formats
- 🧪 Easy testing and demonstration

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Image Processing:** Pillow (PIL)
- **Other Libraries:** NumPy
- **Tools:** Git, GitHub

## 🧩 Project Structure
steganography-project/
│
├── app.py
├── steganography.py
├── init_db.py
├── templates/
│ ├── login.html
| ├── index.html
│ ├── encode.html
│ ├── decode.html
| ├── register.html
│ ├── dashboard.html
│ └── result.html
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
| | └── flash.js
| | └── progress.js
├── screenshots/
│ ├── LandingPage.png
│ ├── Login.png
│ ├── Register.png
│ ├── Encode.png
│ ├── Decode.png
│ ├── Encoded_result.png
│ └── Decoded_result.png
├── README.md
└── requirements.txt


---

## 🚀 How It Works
### Encoding Process
1. User selects a cover image.
2. User enters a secret message or selects a secret image.
3. The data is embedded into the image using steganography techniques.
4. A new **stego image** is generated.

### Decoding Process
1. User uploads the stego image.
2. The hidden data is extracted and displayed.

## 🧪 Screenshots
All application screenshots are available in the **`screenshots/`** folder for better understanding of the UI and workflow.

## 🎥 Demo Video
📎 A complete working demo of the project is available here:  
👉 **Demo Link:** https://drive.google.com/file/d/1AaluppN5TcYt452ajHdd9WoC49CQtbdr/view?usp=drivesdk

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Navigate to the project folder:
cd steganography-project

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
python app.py

5. Open browser and visit:
http://127.0.0.1:5000

## 📚 Use Cases
Secure communication
Data privacy demonstrations
Academic learning and research
Cyber security and information hiding concepts

## 🎓 Academic Purpose

This project was developed as part of EDUNET FOUNDATION - IBM SKILLSBUILD - CYBER SECURITY - 6 WEEKS INTERNSHIP MAY 2025 to understand:
Image processing
Secure data hiding
Web application development using Flask

## 👩‍💻 Author
Pantham Bhavya
B.Tech – Computer Science (AI & ML)
Sridevi Women’s Engineering College

## 📄 License
This project is for educational purposes only.