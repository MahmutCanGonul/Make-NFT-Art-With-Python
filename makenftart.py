Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
from PIL import Image

array = ['C:\choc.png','C:\mario.jpg','C:\goal.jpg']

def convertpixelart(image, i_size, o_size):
    """
    image: path to image file
    i_size: size of the small image eg:(8,8)
    o_size: output size eg:(10000,10000)
    """
    #read file
    img=Image.open(image)

    #convert to small image
    small_img=img.resize(i_size,Image.BILINEAR)

    #resize to output size
    res=small_img.resize(img.size, Image.NEAREST)

    #Save output image
    """
    filename=f'mario_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)
    """
    
    #Display images side by side
    plt.figure(figsize=(16,10))
    #original image
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(img)   #display image
    plt.axis('off')   #hide axis
    #pixel art
    plt.subplot(1,2,2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.show()


for i in range(len(array)):
    if array[i] == 'C:\goal.jpg':
        convertpixelart(image=array[i],i_size=(32 *3 ,32 *3),o_size=img.size)
    else:
        convertpixelart(image=array[i],i_size=(32,32),o_size=img.size)
