# importing the ImageSequence module:
from PIL import Image, ImageSequence
from PIL import Image, ImageFont, ImageDraw

# Opening the input gif:
im = Image.open("GIF.gif")

# create an index variable:
i = 1

# iterate over the frames of the gif:
for img in ImageSequence.Iterator(im):
	font = ImageFont.truetype('calibril.ttf', 44)

	text = "Img Seq Process: " + str(i)
	image = ImageDraw.Draw(img)

	image.text((115, 145), text, (237, 230, 211), font=font, align="left", anchor="ma")


	img.save("Img%d.png"%i)



	i = i + 1
