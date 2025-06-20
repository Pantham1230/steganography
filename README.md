# 🕵️‍♀️ Steganography Web App

A Flask-based web application that allows users to **securely hide and retrieve messages** inside images using the **Least Significant Bit (LSB)** steganography technique.

---

## 🚀 Features

- 🔐 **User Authentication**: Login and registration system with SQLite backend.
- 📥 **Encode Mode**: Embed secret text inside cover images (PNG or JPG).
- 🕵️‍♂️ **Decode Mode**: Extract hidden messages from encoded images.
- 📸 **Image Upload Handling**: File size validation and secure image saving.
- 💾 **Database**: SQLite for user account management.
- 💡 **Clean UI**: Simple interface using HTML, CSS, and optionally Bootstrap.

---

## 🧠 How It Works

### 🔹 Encoding Algorithm
1. Convert input message to binary.
2. Replace the LSB of red channel values in each pixel with message bits.
3. Add a `$$end` marker to indicate the end of the message.
4. Save the modified image as a **stego image**.

### 🔹 Decoding Algorithm
1. Read LSBs from the red channel of each pixel.
2. Reconstruct binary string and convert it to characters.
3. Stop when `$$end` is detected.
4. Display the secret message.

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- Pillow (PIL)
- SQLite3
- HTML5 & CSS3
- Bootstrap 5 *(optional)*

---

## 📦 Installation

### 🔧 Clone the Repository
```bash
git clone https://github.com/Pantham1230/steganography.git
cd steganography

 Author
Pantham Bhavya
https://www.linkedin.com/in/pantham-bhavya