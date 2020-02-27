from PIL import Image
from colors import rgb, hex
import binascii as t
#
def rgb2hex(r,g,b):
    return '{:02x}{:02x}{:02x}'.format(r,g,b)


def hex2rgb(hexa):
    return tuple(hex(hexa).rgb)

def str2binary(str1):
#    str1 = str1.split(' ')
#    str1 = ''.join(str1)
    x=[]
    y='0'
    for i in str1:
        if(i==' '):
            x.append('00100000')
        else:
            
            if(len(format(ord(i),'b'))==8):    
                x.append(format(ord(i),'b'))
#                print('8 : ',x)
            else:
                te=len(format(ord(i),'b'))
                z=format(ord(i),'b')
#                print('before : ',z)
                while(te<8):
                    z = y + z
#                    print(z)
                    te+=1
#                print('<8: ',z)
                x.append(z)
    
    res = ''.join(x)
#    print(res)
    
#    
#    res = ''.join(format(ord(i),'b') for i in str1)
#    print('2: ',res)
    return res

def binary2str(binary):
    str_data =''
#    for i in range(0, len(bin_data), 7):
#        if(bin_data[i:i+8]=='00100000'):
#            str_data = str_data + chr(BinaryToDecimal(int(bin_data[i:i+8])))
#        temp_data = int(bin_data[i:i + 7]) 
#        print(temp_data)
#        decimal_data = BinaryToDecimal(temp_data) 
#        print(decimal_data)
#        str_data = str_data + chr(decimal_data)   
#    return  str_data 
    for i in range(0,len(binary),8):
        str_data = str_data + chr(BinaryToDecimal(int(binary[i:i+8])))
    return str_data



def encode(hexa,digit):
#    print(hexa)
    if(hexa[-1] in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')):
        hexa = hexa[:-1] + digit
#        print('after : ',hexa)
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
#    im2  = im.copy()
    binary = str(str2binary(input('Enter the text you want to hide inside the text : ')) + '1111111111111110')
#    print('str1 : ',binary)
    if(im.mode in ('RGBA')):
        im = im.convert('RGBA')
        rgbarray = (im.getdata())
#        print(rgbarray)
        j=0
        newarray = []
        x=[]
        for i in rgbarray:
            if(j<len(binary)):
                new = encode(rgb2hex(i[0],i[1],i[2]),binary[j])
#                print('new : ',new)
                x.append(new)
                if(new == None):
                    newarray.append(i)
                else:
                    r,g,b = hex2rgb(new)
                    newarray.append((r,g,b,255))
                    j+=1
            else:
                newarray.append(i)
#        for i in range(90):
#            print(i+1,')')
#            print('new : ' ,rgb2hex(newarray[i][0],newarray[i][1],newarray[i][2]))
#            print('old : ' ,rgb2hex(rgbarray[i][0],rgbarray[i][1],rgbarray[i][1]))
#            print('\n')
#        for i in newarray:
#            print('new : ' ,rgb2hex(i[0],i[1],i[2]))
        
        
        im.putdata(newarray)
        im.save(filename,'PNG')
        im.show()     
        
#        im3 = Image.open(filename)
#        data = im3.getdata()
#        for i in range(70):
#            print('new : ',rgb2hex(data[i][0],data[i][1],data[i][2]))
        

def decrypt(filename):
    im = Image.open(filename)
    binary = ''
    if im.mode in ('RGBA'):
        im = im.convert('RGBA')
        rgbarray = (im.getdata())
#        for i in range(90):
#            print('new : ',rgb2hex(rgbarray[i][0],rgbarray[i][1],rgbarray[i][2]))
        for i in rgbarray:
            digit = decode(rgb2hex(i[0],i[1],i[2]))
#            print('digit : ',digit)
            if digit == None:
                pass
            else:
#                print('digit : ',digit)
                binary = binary + digit
                if(binary[-16:]=='1111111111111110'):
#                    print(rgb2hex(i[0],i[1],i[2]))
#                    print('hello' , binary[:-16])
                    return binary2str(binary[:-16])
        return binary2str(binary)
    return 'InCorrect Image Mode..'     
            

x=input('Enter the path of the image with the extension : ')			
encrypt(x)
print(decrypt(x))