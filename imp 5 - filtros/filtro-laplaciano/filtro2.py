from PIL import Image

img = Image.open("filtros (imp 5)\\laplaciano\\dog.jpg")
grayscale_image = img.convert('L')
grayscale_image.save('filtros (imp 5)\\laplaciano\\grayscale-dog.jpg')

second_image = grayscale_image

width, height = grayscale_image.size
second_filter = [[0,-1,0],[-1,4,-1],[0,-1,0]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        second_image_new_value = 0

        for k in range(3):
            for l in range(3):
                second_image_new_value += grayscale_image.getpixel((k+i,l+j)) * second_filter[k][l]

        if (second_image_new_value < 0): 
            second_image_new_value = 0

        second_image.putpixel((i,j), second_image_new_value)

second_image.save("filtros (imp 5)\\laplaciano\\second-laplacian-dog.jpg")