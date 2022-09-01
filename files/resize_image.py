from PIL import Image


imgs = [
'exam.jpg'

]

basewidth = 300

def convert_to(img):
	
	image = Image.open(img)
	wper = (basewidth / float(image.size[0]))
	hsize = int((float(image.size[1]) * float(wper)))
	new = image.resize((basewidth,hsize), Image.ANTIALIAS)
	new.save(img + '300.jpg')

for im in imgs:
	convert_to(im)
