from PIL import Image

def encode_image(cover_path, secret_message, output_path):
    img = Image.open(cover_path).convert('RGB')
    binary_msg = ''.join([format(ord(c), '08b') for c in secret_message + "$$end"])
    pixels = img.load()
    i = 0

    for y in range(img.height):
        for x in range(img.width):
            if i < len(binary_msg):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_msg[i])
                i += 1
                pixels[x, y] = (r, g, b)
            else:
                img.save(output_path)
                return

def decode_image(image_path):
    img = Image.open(image_path)
    binary = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]
            binary += str(r & 1)

    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""
    for c in chars:
        message += chr(int(c, 2))
        if "$$end" in message:
            return message.replace("$$end", "")

    return "❌ No hidden message found or image was not encoded properly."