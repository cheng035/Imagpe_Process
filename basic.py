
from PIL import Image
import numpy as np
# to reduce the image intensity level
## Intensity refers to the amount of light or the numerical value of a pixel. For example, in grayscale images,
# it's depicted by the grey level value at each pixel (e.g., 127 is darker than 220) .
def change_image_intensity(url,level):
    a = np.array(Image.open(url))
    b = a//level*level
    im = Image.fromarray(b.astype('uint8'))
    im.save('2.jpg')

def blur_image()
image_intensity('1.jpg',2)


