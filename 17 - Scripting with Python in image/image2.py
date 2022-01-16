from PIL import Image, ImageFilter
img = Image.open("nam.jpg")
img.thumbnail((400, 400))
img.save('new.jpg')
print(img.size)
