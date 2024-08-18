from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('oboe-with-book.jpg')
plt.imshow(img)

imggray = img.convert('LA')
# 'L' etle Luminance -> tivrata of light 
# 'A' elte Alpha -> transparancy of light
plt.imshow(imggray)

imgmat = np.array(list(imggray.getdata(band=0)), dtype=float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)

plt.imshow(imgmat, cmap='gray')

U ,sigma, V = np.linalg.svd(imgmat)

i = 64 #how much img will be compressed
reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
plt.imshow(reconstimg, cmap='gray')
title = "n = %s" % i
plt.title(title)
plt.show()
    
width , height = img.size
print(f"original resolution: {height} X {width} = {height*width}")
print(f"compression resolution: {height*i} + {i} + {width*i} = {(height*i)+(i)+(width*i)}")
print(f"total reduction = {(100*((height*i)+(i)+(width*i)))/(height*width)}%")