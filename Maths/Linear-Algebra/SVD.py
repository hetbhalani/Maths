from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('oboe-with-book.jpg')
plt.imshow(img)

imggray = img.convert('LA')
# 'L' etle Luminance -> tivrata of light 
# 'A' elte Alpha -> transparancy of light
plt.imshow(imggray)

plt.show()