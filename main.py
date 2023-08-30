from modules.images_processing import *

img = imread('img/4.jpg')
img = thresh(img, 130)
#histo = hist(img)
#showhist(histo)
#img = contrast(img, 10, 10)
imshow(img)
print(nchannels(img))
print(size(img))
