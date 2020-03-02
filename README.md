# Image-Stegnography-using-LSB
	To hide text inside an image using Least significant bit (LSB) method solved using python. 

# Overview
  &nbsp;&nbsp;&nbsp;&nbsp;Every image is made up of pixels. Every pixel is made up of three colors Red, Green, Blue (R, G, B). Now we get a text and convert it into binary. Similarly, we convert the RGB values into binary. Then in the least significant bit of the RGB value, we place the every binary bit of the text one by one. Similarly, we place all the bits of the text in the RGB value of each pixel. Then we add a constraint to show that the text ends at a particular point of time. Thus we hide the text inside the image.
  ![Image-Stegnography-using-LSB](https://2.bp.blogspot.com/-1leyDfJnMJY/WnHSU_aHZKI/AAAAAAAADsk/kClYV86bTwYbIttMrDR2igWNZI_qqJWrwCLcBGAs/s1600/encode.png)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;While decrypting we check the LSB of every pixel’s RGB value and stops when it reaches a constraint. Then convert the binary values that have been got from the RGB values into a string and print it. 
![Image-Stegnography-using-LSB](https://www.pantechsolutions.net/media/catalog/product/cache/1/thumbnail/350x/9df78eab33525d08d6e5fb8d27136e95/m/a/matlab_code_for_lsb_steganography.jpg)
# Requirements
Python 3 and above.  
An image and its path.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;Modules:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colors  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PIL  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;binascii  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Installation of modules:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do the following commands in the command prompt.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install colors  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install PIL  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install binasci  
	

