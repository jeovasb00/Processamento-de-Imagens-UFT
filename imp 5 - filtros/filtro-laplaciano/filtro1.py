from PIL import Image

img = Image.open("filtros (imp 5)\\laplaciano\\dog.jpg")
grayscale_image = img.convert('L')
grayscale_image.save('filtros (imp 5)\\laplaciano\\grayscale-dog.jpg')

first_image = grayscale_image

width, height = grayscale_image.size
first_filter = [[0,1,0],[1,-4,1],[0,1,0]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        first_image_new_value = 0

        for k in range(3):
            for l in range(3):
                first_image_new_value += grayscale_image.getpixel((k+i,l+j)) * first_filter[k][l]

        if (first_image_new_value < 0): 
            first_image_new_value = 0

        first_image.putpixel((i,j), first_image_new_value)

first_image.save("filtros (imp 5)\\laplaciano\\first-laplacian-dog.jpg")