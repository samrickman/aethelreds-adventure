# This script is a modified version of https://github.com/nikhilkumarsingh/terminal-image-viewer/blob/master/img-viewer.py
# I have made some changes:
# # 1. Changed magic numbers to mess around with contrast
# # 2. Change the image size
# # 3. Give the main function arguments that can be changed by other scripts 
# # 4. Taken out re-sizing which I do in GIMP as PIL resize is too fuzzy
# # 5. Mae output twice as wide
import sys
import numpy as np
from PIL import Image

def get_ansi_color_code(r, g, b):


    # Make close to black look black (currently too grey on Windows 10)
    BLACK_THRESHOLD = 70
    if r <  BLACK_THRESHOLD and g < BLACK_THRESHOLD and b < BLACK_THRESHOLD:
        return 0

    if r == g and g == b:
        if r < 8:
            return 0
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 231
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)

# multiplied by 2 to make image wider
def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))*2

def show_image(img_path = "img/rat.png", h = 30):
	try:
		img = Image.open(img_path)
	except FileNotFoundError:
		exit('Image not found.')

	w = int((img.width / img.height) * h) * 2

	#img = img.resize((w,h), Image.ANTIALIAS)
	img_arr = np.asarray(img)
	h,w,c = img_arr.shape

	for x in range(h):
	    for y in range(w):
	        pix = img_arr[x][y]
	        print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
	    print()


if __name__ == '__main__':
	if len(sys.argv) > 1:
		img_path = sys.argv[1]
		show_image(img_path)
	else:
		show_image()