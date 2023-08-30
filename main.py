from module.teste import *

img = imreadgray('img/1.jpg')
#histo = hist(img)
#showhist(histo)
#img = contrast(img, 10, 10)
img = erode(img, seSquare3())
imshow(img)
print(nchannels(img))
print(size(img))
