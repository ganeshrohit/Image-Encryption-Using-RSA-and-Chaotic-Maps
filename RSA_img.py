"""
@authors: Ganesh Rohit Basam, Gayathri Ravipati, Laxman Jagarlamudi, Vennela Chava
"""

from PIL import Image
import random
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage import color, io

cwd_path = os.getcwd()
print("path: ", cwd_path)
image_path = cwd_path + '/test_copy.png'
clrimg = io.imread(image_path)
imgplot = plt.imshow(clrimg)
plt.show()


imgclr_1D = clrimg.ravel() 


### GCD Function

def CalculateGcd(i,j):
    temp = i%j
    while(temp != 0):
        i = j
        j = temp
        temp = i%j

    return j
    

# Selecting the two Prime Numbers as Big as possible
p1 = 37
p2 = 23
n = p1*p2
totientValue = (p1-1)*(p2-1)

# Initially selecting a value of e between 1 and the totient value
e = random.randrange(1, totientValue)  


#Using GCD to verify if e and totient(phi(n)) are comprime or not
# If not select a new value of e
gcdVal = CalculateGcd(e, totientValue)
while gcdVal != 1:
    e = random.randrange(1, totientValue)
    gcdVal = CalculateGcd(e, totientValue)

# To find the  D Value  
def CalculateD(e, phi):
    d = 1
    temp = (d*e)%phi

    while (temp != 1):
        d += 1
        temp = (d*e)%phi

    return d


d = CalculateD(e, totientValue)


# Encryption of the Image values present in the 1d vector
ency = []
for i in range(0, len(imgclr_1D)):
    temp = (int(imgclr_1D[i]) ** e) % n
    ency.append(int(temp))

# Reshaping the 1d vector into the m*n*3 sized array
ency_clrimg = np.array(ency).reshape(clrimg.shape[0], clrimg.shape[1], clrimg.shape[2])
imgplot = plt.imshow(ency_clrimg)
plt.show()

# Decryption of the image:
dec_clr = []
for i in range(0, len(ency)):
    temp = (ency[i] ** d)%n
    dec_clr.append(temp)

#Decrypted Image
decy_img = np.array(dec_clr).reshape(clrimg.shape[0], clrimg.shape[1], clrimg.shape[2])
imgplot = plt.imshow(decy_img)
plt.show()

print("here")



