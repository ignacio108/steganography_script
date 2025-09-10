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
        
        arr_secret= Image.fromarray(a)
        arr_container= Image.fromarray(b)
        print(x)
        print(y)
        print("executing the algorithm")

        for i in range(0,x):
            for j in range(0,y):
                print("Modification of the pixel "+str(i)+" "+str(j))
                

                aux=arr_secret.getpixel((i,j))
                aux2=arr_container.getpixel((i,j))

                for k in range(0,4):

                    
                    #Secreto
                    aux_binary= f"{aux[k]:08b}"
                    aux_4_last_bits=aux_binary[4]+aux_binary[5]+aux_binary[6]+aux_binary[7]

                    #Contenedor    
                    aux2_binary= f"{aux2[k]:08b}"
                    aux2_4_first_bits= aux2_binary[0]+aux2_binary[1]+aux2_binary[2]+aux2_binary[3]
                    

                    final_bytes= aux2_4_first_bits+aux_4_last_bits
                
                
                print(final_bytes)


                  
                #final_image= Image.frombuffer
                print(aux)
                print(aux2)


    


def main():

    change_bits(im1,im2)


if __name__ == "__main__":
    main()