#!/usr/bin/env python3
from PIL import Image
import numpy as np
import argparse




def main():

    parser = argparse.ArgumentParser(description='Script to Hide an image inside another one ')
    parser.add_argument('--secret', default='img/Secret.png',required=True, help='Path to the secret image')
    parser.add_argument('--container', default='img/Secret.png',required=True, help='Path to the container image')
    args = parser.parse_args()  

    im1 = Image.open(args.secret)
    im2 = Image.open(args.container)


    if(size_check(im1,im2)):
    
        new_image= change_bits(im1,im2)
        new_image.save("img/out.png")

    else:
        print("The images have diferrent sizes")


#Function to check the sizes of an image
def size_check(secret,container):
    if(secret.size != container.size):
        return False
    else:
        return True
    

'''
Attributes:

-secret: the image that will be "inside" the container image"

-cointainer: the image that will be used as a container 

Algorithm:

1º We need to eliminate the least significant byte for the cointainer for each pixel

2º We obtain the most significant byte from the secret image 

3º We put the most significant byte of our secret image in the least significant byte of the container image



Return:

The new image


'''

def change_bits(secret,container):



    #Now we can assure that the size is the same let's procced to obtain the values of the size for the loop
    
    a = np.asarray(secret)
    b = np.asarray(container)

    arr_secret= Image.fromarray(a)
    arr_container= Image.fromarray(b)

    x= secret.size[0]
    y= container.size[1]



    new_img = Image.new('RGBA', (x, y))
    print("executing the algorithm")

    for i in range(0,secret.size[0]):
        for j in range(0,secret.size[1]):
            #print("Modification of the pixel "+str(i)+" "+str(j))
            

            aux_secret=arr_secret.getpixel((i,j))
            aux_container=arr_container.getpixel((i,j))
            new_pixel=[]

            for k in range(0,4):

                
                #Secreto
                aux_secret_binary= f"{aux_secret[k]:08b}"
                aux_4_last_bits=aux_secret_binary[0]+aux_secret_binary[1]+aux_secret_binary[2]+aux_secret_binary[3]

                #Contenedor    
                aux_container_binary= f"{aux_container[k]:08b}"
                aux_4_first_bits= aux_container_binary[0]+aux_container_binary[1]+aux_container_binary[2]+aux_container_binary[3]
                #Script hecho por Ignacio ;)

                final_bytes= aux_4_first_bits+aux_4_last_bits
            
                final_bytes_dec=int(final_bytes,2)
                new_pixel.append(final_bytes_dec)
            
            position=(i,j)
            new_img.putpixel(position,tuple(new_pixel))
    return new_img
    

if __name__ == "__main__":
    main()