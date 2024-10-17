from PIL import Image

def convert(img, newImg, i, j):
    r, g, b = img.getpixel((i,j))
    newR = abs(r-255)
    newG = abs(g-255)
    newB = abs(b-255)
    newImg.putpixel((i,j), (newR, newG, newB))

img = Image.open('P1trab2/img1.jpg')
width, height = img.size

newImg = Image.new(mode = "RGB", size = (width, height))

for i in range(width):
    for j in range(height):
        convert(img, newImg, i, j)

newImg.save("img-negative.jpg")