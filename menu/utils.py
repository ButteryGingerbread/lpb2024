import base64

# To encode an image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# To decode an image
def decode_image(encoded_image, output_path):
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(encoded_image))
