from PIL import Image

img = Image.open("imp 5 - filtros\\filtro-gradiente\\dog.jpg")
grayscale_image = img.convert('L')
grayscale_image.save('imp 5 - filtros\\filtro-gradiente\\grayscale-dog.jpg')

first_image = grayscale_image

width, height = grayscale_image.size
first_filter = [[-1,-2,-1],[0,0,0],[1,2,1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        first_image_new_value = 0

        for k in range(3):
            for l in range(3):
                first_image_new_value += grayscale_image.getpixel((k+i,l+j)) * first_filter[k][l]

        if (first_image_new_value < 0): 
            first_image_new_value = 0

        first_image.putpixel((i,j), first_image_new_value)

first_image.save("imp 5 - filtros\\filtro-gradiente\\first-sobel-dog.jpg")