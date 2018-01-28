import PIL.Image as img

from src.BicubicEnhance import bicubic


def load(path):
	image = img.open(path)
	image.show()
	return image

image = load("assets/test2.jpg")
bicubic(image)
