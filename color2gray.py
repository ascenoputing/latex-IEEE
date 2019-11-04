from PIL import  Image

image = 'a3.jpg'

rgb_img = Image.open(image) 

grey_img = rgb_img.convert('L')

grey_img.save(image.split('.')[0]+'.png')


