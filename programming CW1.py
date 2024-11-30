# By: Yassin Ahmed, ID: 202300080

def encode_message(image_path, message, output_path):
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
    with open(output_path, 'wb') as output:
        output.write(data)

    print("Message successfully hidden in 'Hidden msg.bmp'")

def decode_message(image_path):
    #Read the BMP file 
    with open(image_path, 'rb') as img:
        data = bytearray(img.read())
    
    #extracting message from image's data
    msg_bytes = bytearray()
    #skiping the first 54 bytes
    for i in range((len(data) - 54) // 8): 
        byte = 0
        for bit in range(8):
            index = 54 + i * 8 + bit
            byte = (byte << 1) | (data[index] & 0x01)
        # Check if the constructed byte is the null terminator 0
        if byte == 0:  
            break
        msg_bytes.append(byte)

    #Convert byte array to string
    hidden_msg = msg_bytes.decode('utf-8')
    return hidden_msg

if __name__ == "__main__":
    img_path = input("Enter the BMP image path: ")
    output_img_path = "Hidden msg.bmp"
    secret_msg = input("Enter the message to hide: ")

    # Hide the message in the BMP file
    encode_message(img_path, secret_msg, output_img_path)

     # Decode and verify the hidden message
    decoded_message = decode_message(output_img_path)
    print(f"Decoded message: {decoded_message}")
    





