from module.teste import teste
from module.bilioteca import *

img = imread('img\hora_aventura.jpg')
#histo = hist(img)
#showhist(histo)
#img = contrast(img, 10, 10)
imshow(img)
print(nchannels(img))
print(size(img))
