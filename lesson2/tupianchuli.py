from __future__ import print_function
from PIL import Image

def tupianchuli():
    im = Image.open('mytargit.jpg')
    HEIGHT = 40
    WEIDTH = 60
    im = im.resize((WEIDTH,HEIGHT))

    grey_list = list("@#$%&MZwm=Va+u6pqds3*(?tiO{[!/<>o;:)'.—-")
    def my_paint(r, g, b, alpha = 256):
        if (alpha == 0):
            return ' '
        ulen = (256 + 1) / len(grey_list)
        grey = int(r*0.2126 + g*0.7152 + b*0.0722)
        return grey_list[int(grey / ulen)]

    i = 0
    body = ""
    while (i < HEIGHT):
        j = 0
        while (j < WEIDTH):
            body += my_paint(*im.getpixel((j,i)))
            j += 1
        body += '\n'
        i += 1
    print (body)