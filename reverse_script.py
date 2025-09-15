#!/usr/bin/env python3 
from PIL import Image
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser(description=" Script to reveal the secret image of a container image")
    parser.add_argument('--image',required=True,help="Path to the image containing the secret image")
    args = parser.parse_args()

    im1 = Image.open(args.image)
    new_image= reveal_secret(im1)
    new_image.save("img/secret_revealed.png")




def reveal_secret(image):

    a = np.asarray(image)

    arr_image = Image.fromarray(a)

    x= image.size[0]
    y= image.size[1]

    new_img = Image.new('RGBA',(x,y))

    for i in range (0, image.size[0]):
        for j in range (0, image.size[1]):

            aux=arr_image.getpixel((i,j))
            new_pixel = []

            for k in range(0,4):

                aux_binary = f"{aux[k]:08b}"
                
                aux_binary_pixel= aux_binary[4]+aux_binary[5]+aux_binary[6]+aux_binary[7]+'0000'


                final_byte_dec=int(aux_binary_pixel,2)
                new_pixel.append(final_byte_dec)

            position = (i,j)
            new_img.putpixel(position,tuple(new_pixel))
    return new_img



if __name__ == "__main__":
    main()
