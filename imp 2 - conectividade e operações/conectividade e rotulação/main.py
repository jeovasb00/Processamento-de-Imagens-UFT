import random
from PIL import Image

img = Image.open('conectividade e rotulação/img.jpg')
width, height = img.size

def binImg(img, limit):
    bin = img
    for i in range(width):
        for j in range(height):
            R, G, B = img.getpixel((i, j))
            if ((R + G + B)/3 <= limit):
                bin.putpixel((i,j), (0, 0, 0))
            else:
                bin.putpixel((i,j), (255, 255, 255))
    return bin

bin_img = binImg(img, 200)
bin_img.save('bin-img.jpg')

labeled_img = bin_img

for i in range(1, width):
    for j in range(1, height):
        s = bin_img.getpixel((i - 1, j))
        r = bin_img.getpixel((i, j - 1))
        p = bin_img.getpixel((i, j))
        if p == (0, 0, 0):
            if s == (255, 255, 255) and r == (255, 255, 255):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                labeled_img.putpixel((i, j), (r, g, b))
            elif s != r:
                if s != (255, 255, 255):
                    labeled_img.putpixel((i, j), labeled_img.getpixel((i - 1, j)))
                elif r != (255, 255, 255):
                    labeled_img.putpixel((i, j), labeled_img.getpixel((i, j - 1)))
            elif (s == r != (255, 255, 255)) and (labeled_img.getpixel((i - 1, j)) == labeled_img.getpixel((i, j - 1))):
                labeled_img.putpixel( (i, j), labeled_img.getpixel((i, j - 1)) )
            elif (s == r != (255, 255, 255)) and (labeled_img.getpixel((i - 1, j)) != labeled_img.getpixel((i, j - 1))):
                labeled_img.putpixel( (i, j), labeled_img.getpixel((i, j - 1)) )
                labeled_img.putpixel( (i-1, j), labeled_img.getpixel((i, j - 1)) )
            
labeled_img.save('labeled-img.jpg')