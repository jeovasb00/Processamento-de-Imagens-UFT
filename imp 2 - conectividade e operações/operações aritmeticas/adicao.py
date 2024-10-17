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

        newImg.putpixel((i,j), (int((pR+qR)/2), int((pG+qG)/2), int((pB+qB)/2)))

newImg.save("sum-img.jpg")