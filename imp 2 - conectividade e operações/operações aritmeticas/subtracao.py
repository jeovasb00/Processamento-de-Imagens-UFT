from PIL import Image

img1 = Image.open('operações aritmeticas/img1.jpg')
img2 = Image.open('operações aritmeticas/img2.jpg')
img1Width, img1Height = img1.size
img2Width, img2Height = img2.size


width = max(img1Width, img2Width)
height = max(img1Height, img2Height)
newImg = Image.new(mode = "RGB", size = (width, height))

for i in range(width):
    for j in range(height):
        pR, pG, pB = img1.getpixel((i,j))
        qR, qG, qB = img2.getpixel((i,j))
        
        if pR == qR and pG == qG and pB == qB:
            r = pR
            g = pG
            b = pB
        else:
            r = pR - qR  
            g = pG - qG  
            b = pB - qB  


        newImg.putpixel((i,j), (r,g,b))

newImg.save("subtraction-img.jpg")