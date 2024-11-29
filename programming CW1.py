# By: Yassin Ahmed, ID: 202300080

def encode_message(image_path, message):
    # Read the BMP file
    with open(image_path, 'rb') as img:
        data = bytearray(img.read())

    # add a null terminator to the end of the message
    message += '\0'
    msg_bytes = bytearray(message, 'utf-8')

    # Error handling that Excludes the BMP header
    if len(msg_bytes) * 8 > len(data) - 54:  
        raise ValueError("The message is too long to hide in this image.")


    # Embed the message
    for i in range(len(msg_bytes)):
        for bit in range(8):
            idx = 54 + i * 8 + bit
            data[idx] = (data[idx] & 0xFE) | ((msg_bytes[i] >> (7 - bit)) & 0x01)

    # output to a new file
    with open("Hidden.bmp", 'wb') as output:
        output.write(data)

    print("Message successfully hidden in 'Hidden.bmp'")

if __name__ == "__main__":
    img_path = input("Enter the BMP image path: ")
    secret_msg = input("Enter the message to hide: ")
    encode_message(img_path, secret_msg)