#!/usr/bin/env python3
import os, sys
from PIL import Image
import numpy as np



im1 = Image.open("img/Prueba.png")
im2 = Image.open("img/Prueba2.png")
a = np.asarray(im1)
b = np.asarray(im2)


#This is the function to change the pixels
'''
1º We need to eliminate the least significant byte for the cointainer for each pixel

2º We obtain the most significant byte from the secret image 

3º We put the most significant byte of our secret image in the lest significant byte of the container image


'''
def change_bits(secret,container):

    if(im1.size != im2.size):
        print("The images must have the same size")
    
    else:

        #Now we can assure that the size is the same let's procced to obtain the values of the size for the loop
        
        x=im1.size[0]
        y=im1.size[1]
        
        print(x)
        print(y)
        print("executing the algorithm")

        for i in range(0,x):
            for j in range(0,y):
                print("Modification of the pixel "+str(i)+" "+str(j))
                print("xxx")


        arr_secret= Image.fromarray(a)
        print(im1.size)
        print(arr_secret.getpixel((0,0)))
        print(im2.size)


def main():

    change_bits(im1,im2)


if __name__ == "__main__":
    main()