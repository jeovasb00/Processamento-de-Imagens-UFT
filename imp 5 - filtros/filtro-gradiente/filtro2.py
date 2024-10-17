from PIL import Image

img = Image.open("imp 5 - filtros\\filtro-gradiente\\dog.jpg")
grayscale_image = img.convert('L')
grayscale_image.save('imp 5 - filtros\\filtro-gradiente\\grayscale-dog.jpg')

second_image = grayscale_image

width, height = grayscale_image.size
second_filter = [[-1,0,1],[-2,0,2],[-1,0,1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        second_image_new_value = 0

        for k in range(3):
            for l in range(3):
                second_image_new_value += grayscale_image.getpixel((k+i,l+j)) * second_filter[k][l]

        if (second_image_new_value < 0): 
            second_image_new_value = 0

        second_image.putpixel((i,j), second_image_new_value)

second_image.save("imp 5 - filtros\\gradiente\\second-sobel-dog.jpg")