from PIL import Image
from colors import rgb, hex
import binascii as t

def rgb2hex(r,g,b):
    return '{:02x}{:02x}{:02x}'.format(r,g,b)


def hex2rgb(hexa):
    return tuple(hex(hexa).rgb)

def str2binary(str1):
    x=[]
    y='0'
    for i in str1:
        if(i==' '):
            x.append('00100000')
        else:
            
            if(len(format(ord(i),'b'))==8):    
                x.append(format(ord(i),'b'))
            else:
                te=len(format(ord(i),'b'))
                z=format(ord(i),'b')
                while(te<8):
                    z = y + z
                    te+=1
                x.append(z)
    
    res = ''.join(x)
    return res

def binary2str(binary):
    str_data =''
    for i in range(0,len(binary),8):
        str_data = str_data + chr(BinaryToDecimal(int(binary[i:i+8])))
    return str_data



def encode(hexa,digit):
    if(hexa[-1] in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')):
        hexa = hexa[:-1] + digit
        return hexa
    else:
        return None
    
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


def encrypt(filename):
    im = Image.open(filename)
    binary = str(str2binary(input('Enter the text you want to hide inside the text : ')) + '1111111111111110')
    if(im.mode in ('RGBA')):
        im = im.convert('RGBA')
        rgbarray = (im.getdata())
        j=0
        newarray = []
        x=[]
        for i in rgbarray:
            if(j<len(binary)):
                new = encode(rgb2hex(i[0],i[1],i[2]),binary[j])
                x.append(new)
                if(new == None):
                    newarray.append(i)
                else:
                    r,g,b = hex2rgb(new)
                    newarray.append((r,g,b,255))
                    j+=1
            else:
                newarray.append(i)
        im.putdata(newarray)
        im.save(filename,'PNG')
        im.show()             

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
            

x=input('Enter the path of the image with the extension : ')			
encrypt(x)
print(decrypt(x))
