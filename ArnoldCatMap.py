"""
@authors: Ganesh Rohit Basam, Gayathri Ravipati, Laxman Jagarlamudi, Vennela Chava
"""

import numpy as np
import os
import cv2 
from skimage import color, io

def readImage(path):
	if os.path.isfile(path)==False:
		raise Exception("Invalid path for the file or the program doesn't have required permissions")
	try:
		img = cv2.imread(path)
	except Exception as i:
		raise i
	else:
		return img

def ApplyArnoldTransform(imageData):
    m = imageData.shape[0]
    n = imageData.shape[1]

    t = max(m,n)

    sampleImage = np.zeros([t,t,3])
    imagePadding = ((0,t-m),(0,t-n),(0,0))

    paddedImg = np.pad(imageData, imagePadding, mode='constant', constant_values=255)

    for i in range(0,t):
        for j in range(0,t):
            sampleImage[i][j] = paddedImg[(2*i+j)%t][(j+i)%t]

    return sampleImage

def ApplyInverseArnoldTransform(imageData):
    m = imageData.shape[0]
    n = imageData.shape[1]

    sampleImage = np.zeros([m,n,3])

    if m != n:
        raise Exception("Supplied Encrypted image is not a square image")

    for i in range(0 , m):
        for j in range(0, m):
            sampleImage[i][j] = imageData[(i-j)%m][((2*j)-i)%m]

    return sampleImage

def encryptImage(imageData, key):
    tempImg = imageData
    for i in range(0,key):
        tempImg = ApplyArnoldTransform(tempImg)
    imageData = tempImg
    return imageData

def decryptImage(imageData, key):
    tempImg = imageData
    for i in range(0,key):
        tempImg = ApplyInverseArnoldTransform(tempImg)
    imageData = tempImg
    return imageData

cwd_path = os.getcwd()
print("path: ", cwd_path)

image_path = cwd_path+ '/test_copy.png'
key = 25

imgclr = readImage(image_path)
cv2.imshow('image view', imgclr)
cv2.waitKey(0)

EncryptedImageData = encryptImage(imgclr, key)
EncryptedWritePath = cwd_path+'/Arnold_Cat_Enc.png'
cv2.imwrite(EncryptedWritePath, EncryptedImageData)
EncryptedImageData = EncryptedImageData.astype(np.uint8)
cv2.imshow('Encrypted image view', EncryptedImageData)
cv2.waitKey(0)

DecryptedImageData = decryptImage(EncryptedImageData, key)
DecryptedWritePath = cwd_path+'/Arnold_Cat_Dec.png'
cv2.imwrite(DecryptedWritePath, DecryptedImageData)
DecryptedImageData = DecryptedImageData.astype(np.uint8)
cv2.imshow('Decrypted image view', DecryptedImageData)
cv2.waitKey(0)




