"""
@authors: Ganesh Rohit Basam, Gayathri Ravipati, Laxman Jagarlamudi, Vennela Chava
"""

from PIL import Image
import numpy as np
import os
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import cv2 
import random
from math import log
     

def readImage(imageName):
    temp_image = Image.open(imageName) 
    imagePixelData = temp_image.load()
    imagems = temp_image.size 
    imagePixelValues = []
    color = 1
    if type(imagePixelData[0,0]) == int:
      color = 0
    for i in range(int(imagems[0])):
        row = []
        for j in range(int(imagems[1])):
                row.append((imagePixelData[i,j]))
        imagePixelValues.append(row)
    return imagePixelValues, imagems[0], imagems[1],color  


def CalculateTotalBitValue(bitSequence):
    value = 0
    for bit in bitSequence:
        value = value * 2 + int(bit)
    return value
     

def genHenonMap(m, key):
    sequenceSize = m * m * 8 
    bitSequence = []  
    byteArray = []  
    TransformMatrixValues = []

    x = key[0]
    y = key[1] 
    for i in range(sequenceSize):
        xN = y + 1 - 1.4 * x**2
        yN = 0.3 * x

        x = xN
        y = yN

        if xN <= 0.4:
            bit = 0
        else:
            bit = 1

        bitSequence.append(bit)

        if i % 8 == 7:
            decimal = CalculateTotalBitValue(bitSequence)
            byteArray.append(decimal)
            bitSequence = []

        byteArraySize = m*8

        if i % byteArraySize == byteArraySize-1:
            TransformMatrixValues.append(byteArray)
            byteArray = []

    return TransformMatrixValues
     

def HenonEncryption(imageName,key):
    imageimagePixelDataelData, m, n, color = readImage(imageName)
    OutPutImage = []
    HenonMapMatrix = genHenonMap(m, key)
    for i in range(m):
        li = []
        for j in range(n):
            if color:
                #print("here: ",tuple([HenonMapMatrix[i][j] ^ x for x in imageimagePixelDataelData[i][j]]))
                li.append(tuple([HenonMapMatrix[i][j] ^ x for x in imageimagePixelDataelData[i][j]]))
            else:
                li.append(HenonMapMatrix[i][j] ^ imageimagePixelDataelData[i][j])
    
        OutPutImage.append(li)

    if color:
      temp_image = Image.new("RGB", (m, n))
    else: 
      temp_image = Image.new("L", (m, n))

    imagePixelData = temp_image.load()
    for x in range(m):
        for y in range(n):
            imagePixelData[x, y] = OutPutImage[x][y]
    temp_image.save(imageName.split('.')[0] + "_HenonEnc.png", "PNG")
     

def HenonDecryption(imageNameEnc, key):
    imageimagePixelDataelData, m, n, color = readImage(imageNameEnc)
    DecryptedImage = []
    HenonMapMatrix = genHenonMap(m, key)

    for i in range(m):
        li = []
        for j in range(n):
            if color:
                li.append(tuple([HenonMapMatrix[i][j] ^ x for x in imageimagePixelDataelData[i][j]]))
            else:
                li.append(HenonMapMatrix[i][j] ^ imageimagePixelDataelData[i][j])

        DecryptedImage.append(li)

    if color:
        temp_image = Image.new("RGB", (m, n))
    else: 
        temp_image = Image.new("L", (m, n)) # L is for Black and white imagePixelDataels

    imagePixelData = temp_image.load()
    for x in range(m):
        for y in range(n):
            imagePixelData[x, y] = DecryptedImage[x][y]
    temp_image.save(imageNameEnc.split('_')[0] + "_HenonDec.png", "PNG")
     

cwd_path = os.getcwd()
print("path: ", cwd_path)

image_path = cwd_path + '/test.png'
image = "test"
ext = ".png"
key = (0.1,0.1)
     

clr_img = Image.open(image_path, 'r')
imshow(np.asarray(clr_img))
plt.show()
img_data = clr_img.load()
print(type(img_data))
print(clr_img.size)

HenonEncryption(image_path, key)
temp_image = Image.open(image + "_HenonEnc.png", 'r')
imshow(np.asarray(temp_image))
plt.show()

HenonDecryption(image + "_HenonEnc.png", key)
temp_image = Image.open(image + "_HenonDec.png", 'r')
imshow(np.asarray(temp_image))
plt.show()