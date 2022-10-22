import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


os.chdir('D:/abhay/')
SAVEDIR = "D:/abhay/wavelets/image/output/"
IMAGEDIR="D:/abhay/wavelets/dataset"


def loadAndProcessImage(fileName):
    inputImage = imread(fileName)[:,:]
    fourier_masker_ver(inputImage, 1)
    
    fileName1 = os.path.basename(fileName)
    fileName1 = os.path.splitext(fileName1)
    fileName2=fileName1[0]
    fileName2=SAVEDIR + fileName2+"_new"
    plt.savefig(str(fileName2)+".png")
    
def fourier_masker_ver(image, i):
    f_size = 15
    fourierImage = np.fft.fftshift(np.fft.fft2(image))
    fourierImage[:225, 235:240] = i
    fourierImage[-225:,235:240] = i
    fig, ax = plt.subplots(1,3,figsize=(15,15))
    ax[0].imshow(np.log(abs(fourierImage)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize = f_size)
    ax[1].imshow(image, cmap = 'gray')
    ax[1].set_title('Original Image', fontsize = f_size)
    ax[2].imshow(abs(np.fft.ifft2(fourierImage)), 
                     cmap='gray')
    ax[2].set_title('Transformed Image', 
                     fontsize = f_size)

#main

dirpath = os.listdir(IMAGEDIR)

for subdir in dirpath:
    full_subdir= IMAGEDIR + '/' + subdir + '/'
    imageList = os.listdir(full_subdir)
    for image in imageList:
        fullpath = full_subdir + image
        loadAndProcessImage(fullpath)




    
