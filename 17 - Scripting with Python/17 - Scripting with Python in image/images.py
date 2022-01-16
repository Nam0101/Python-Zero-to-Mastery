from PIL import Image, ImageFilter
img = Image.open(
    '17 - Scripting with Python\Images With Python\pokedex\pikachu.jpg')
filtered_image = img.filter(ImageFilter.SHARPEN)
# crop=filtered_image.rotate(90)
resized_image=img.resize((300,300))
box=(100,100,400,400)
region=resized_image.crop(box)

filtered_image.save("blur.png", 'png')
region.show()
# img2=img.convert('L')
# img2.save("grey.png", 'png')