from PIL import Image, ImageEnhance

# Opening Image
im = Image.open("inp.jpg")

# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(im)

# showing resultant image
im3.enhance(25.0).save("sharp.jpg")



im3 = ImageEnhance.Brightness(im)

# showing resultant image
im3.enhance(25.0).save("bright.jpg")

im3 = ImageEnhance.Contrast(im)

# showing resultant image
im3.enhance(25.0).save("contrast.jpg")

im3 = ImageEnhance.Color(im)

# showing resultant image
im3.enhance(25.0).save("color.jpg")

