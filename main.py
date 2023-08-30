from modules.images_processing import *

img = imreadgray('img/1.jpg')
#histo = hist(img)
#showhist(histo)
#img = contrast(img, 10, 10)
imshow(img)
print(nchannels(img))
print(size(img))
