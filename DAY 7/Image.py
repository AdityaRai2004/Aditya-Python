from PIL import Image, ImageOps

# Open the input image
input_image = Image.open("adi.jpg")  # Replace 'example.jpg' with your image file path

# Check if the image mode is not 'RGB' and convert it if necessary
if input_image.mode != 'RGB':
    input_image = input_image.convert('RGB')
inverted_image = ImageOps.invert(input_image)
inverted_image.save("inverted_example.jpg")
input_image.show()
inverted_image.show()
