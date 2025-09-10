# steganography_script
Steganography script to Implementing the LSB method to hide one image in another

## Algorithm
- Opening both images (the hidden image and the container image)
    It Use "import sys" and "from PIL import Image“* then "Image.open“
    *PIL (or Pillow) is the most suitable library for image manipulation in Python
- Create an image that will contain your final image (Image.new)
- Make a loop through each pixel of the image (getpixel)
     Remove least significant bits from the container (use a logical &)
     Shift the most significant bits to the least significant bits of the secret (use a
        shift to the right: >>)
     Add the most significant bits of the container to the least significant bits of the
        secret (use a logical |)
- Save the image in BMP (avoids compression)

