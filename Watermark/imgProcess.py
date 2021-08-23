from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("inp.jpg")
font = ImageFont.truetype('calibril.ttf', 44)

text = input()
image = ImageDraw.Draw(my_image)

image.text((115,145), text, (237, 230, 211), font=font, align = "left", anchor="ma")

my_image.save("watermark.jpg")