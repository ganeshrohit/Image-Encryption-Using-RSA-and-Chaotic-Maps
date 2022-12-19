# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:49:49 2019

@author: Tejas
"""

import random
import numpy as np
import math

# Enter the text message that you want to encrypt
text_msg = 'Hi, I am Tejas, I am doing MS in Artificial Intelligence in Northeastern University, Happy Diwali!!'

### Converting the above message to ascii values
msg_ascii = [ord(letters) for letters in text_msg]

########### RSA Algorithm

### GCD Function
def gcd(a, h):
    while(1):
        temp = a%h
        if(temp == 0):
            return h;
        a = h
        h = temp
    

################# Prime Numbers Big enough
p = 37          ### as high as possible 
q = 23
n = p*q
totient = (p-1)*(q-1)
e = random.randrange(1, totient)  


#Use Euclid's Algorithm to verify that e and phi(n) are comprime
g = gcd(e, totient)
while g != 1:
    e = random.randrange(1, totient)
    g = gcd(e, totient)

### Finding D Value  
def multiplicative_inverse(e, phi):
    d = None
    i = 1
    exit = False
    while not exit:
        temp1 = phi*i +1
        d = float(temp1/e)
        d_int = int(d)
        i += 1
        if(d_int == d):
            exit=True
    return int(d)
       
d = multiplicative_inverse(e, totient)

#### Now we have p,q,n,totient,e,g,d
#### Encryption
# for i in range(0, len(msg_ascii)): then use as msg_ascii[i]
encrypted_list = []
for num in msg_ascii:
    current_enc = (num ** d) % n
    encrypted_list.append(current_enc)
    
enc_chars = []
for num in encrypted_list:
    enc_chars.append(chr(num))

encrypted_msg = ''.join(map(lambda x: str(x), enc_chars))

print(encrypted_msg)


####### Decryption
dec_list = []
for i in range(0, len(encrypted_list)):
    current_dec = (encrypted_list[i] ** e) % n
    dec_list.append(current_dec)

### conerting decrypted msg to characters
chars = []
for num in dec_list:
    chars.append(chr(num))


decrypted_msg = ''.join(map(lambda x: str(x), chars))






