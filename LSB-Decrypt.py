# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:45:28 2020

@author: Raagul
"""

from PIL import Image
from colors import rgb, hex
import binascii as t

def rgb2hex(r,g,b):
    return '{:02x}{:02x}{:02x}'.format(r,g,b)

def binary2str(binary):
    str_data =''
    for i in range(0,len(binary),8):
        str_data = str_data + chr(BinaryToDecimal(int(binary[i:i+8])))
    return str_data


def decode(hexa):
    if hexa[-1] in ('0','1'):
        return hexa[-1]
    else:
        return None

def BinaryToDecimal(binary):  
         
    decimal, i = 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)


def decrypt(filename):
    im = Image.open(filename)
    binary = ''
    if im.mode in ('RGBA'):
        im = im.convert('RGBA')
        rgbarray = (im.getdata())
        for i in rgbarray:
            digit = decode(rgb2hex(i[0],i[1],i[2]))
            if digit == None:
                pass
            else:
                binary = binary + digit
                if(binary[-16:]=='1111111111111110'):
                    return binary2str(binary[:-16])
        return binary2str(binary)
    return 'InCorrect Image Mode..'     


if(__name__=="__main__"):
    x=input('Enter the path of the image with the extension : ')			
    try:
        y=decrypt(x)
        if(y==''):
            print('No text encrypted..')
        else:
            print(y)
    except:
        print('Error.....')
    