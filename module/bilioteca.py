import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import matplotlib.cm as cm
import os

def imread(filename):
    im = mpimg.imread(filename)
    if im.dtype == np.float32:
        im = (im * 255).astype(np.uint8)
    if len(im.shape) >= 3 and im.shape[2] > 3:
        im = im[:, :, 0:3]
    return im

def imshow(im):
    plot = plt.imshow(im, origin="upper")
    plot.set_interpolation('nearest')
    plt.show()

def nchannels(im):
    #print(im.shape)
    if len(im.shape) >= 3:
        return im.shape[2]
    else:
        return 1

def size(im):
    height, width = im.shape[:2]
    return [width, height]

def rgb2gray(im):
    weights = [0.299, 0.587, 0.114]
    gray_image = np.dot(im[..., :3], weights)
    return gray_image.astype(np.uint8)

def imreadgray(filename):
    im = imread(filename)
    if nchannels(im) >= 3:
        gray_image = rgb2gray(im)
    else:
        gray_image = im
        
    return gray_image

def thresh(im, threshold):
    binary_image = np.where(im >= threshold, 255, 0)
    return binary_image.astype(np.uint8)

def negative(im):
    negative_image = 255 - im
    return negative_image.astype(np.uint8)

def contrast(im, r, m):
    g = r * (im - m) + m
    g = np.clip(g, 0, 255)
    return g.astype(np.uint8)

def hist(im):
    if nchannels(im) == 1:
        hist_values = np.bincount(im.flattern(), minlength=256)
    else:
        hist_values = np.column_stack([np.bincount(im[:,:,i].flatten(), minlength=256) for i in range(3)])
    
    return hist_values

def showhist(hist_values, binsize=1):
    if binsize <= 0:
        raise ValueError("O tamanho dos bins deve ser positivo")
    
    hist_length = hist_values.shape[0]
    num_bins = hist_length // binsize
    binned_hist = hist_values[:num_bins * binsize].reshape(num_bins, binsize, -1).sum(axis=1)
    
    if hist_values.shape[1] == 3:
        colors = ['red', 'green', 'blue']
        for i, color in enumerate(colors):
            plt.bar(range(num_bins), binned_hist[:, i], color=color, alpha=0.7, label=color)
    else:  
        plt.bar(range(num_bins), binned_hist, color='gray', alpha=0.7, label='gray')
    
    plt.xlabel('Intervalos de Intensidade')
    plt.ylabel('Frequência')
    plt.legend()
    plt.show()
    if binsize < 1:
        raise ValueError("O valor de binsize deve ser pelo menos 1.")
    
    hist_values_grouped = [sum(hist_values[i:i+binsize]) for i in range(0, len(hist_values), binsize)]
    
    if hist_values.shape[1] == 3:  
        colors = ['red', 'green', 'blue']
        for i, color in enumerate(colors):
            plt.bar(range(0, 256, binsize), hist_values_grouped[i::3], color=color, alpha=0.7, label=color)
    else:  
        plt.bar(range(0, 256, binsize), hist_values_grouped, color='gray', alpha=0.7, label='gray')
    
    plt.xlabel('Intensidade de Cinza')
    plt.ylabel('Frequência')
    plt.legend()
    plt.show()
