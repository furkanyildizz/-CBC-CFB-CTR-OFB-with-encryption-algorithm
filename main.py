__author__ = 'Furkan Yildiz, Ali Eken, Eren Berk Edinc, Ugur Samet Satir'

import unittest
from aes import AES
from clefia import sifreleClefia
from clefia import desifreleClefia
import gost
import katan
import ktantan
import random
import ofb
import ctr
import cfb
import cbc



#deneme.assertEqual(decrypted, 0x3243f6a8885a308d313198a2e0370734)

#text to hex lazim
#16byte olarak bolunmesi lazim

"""
girilentext="Selamin aleykumm"
#print(deneme1234.encode("hex"))
hexlendi=girilentext.encode("hex")
print("hadi la",hexlendi)
hexoldu = int(hexlendi, base=16)
print("convetstring","%x" % hexoldu)
"""


secenek = raw_input("AES:1 "+" "+" CLEFIA:2 "+" "+"GOST:3 "+" "+" KATAN:4 "+" "+"KTANTAN:5 ")
secenek2=raw_input("CBC:1 "+" "+" CFB:2 "+" "+"OFB:3 "+" "+" CTR:4 ")
secenek3=raw_input("TEXT: ")
print("Secilen ALGORITMA",secenek)
print("Secilen MOD",secenek2)


if secenek=="1" :
    
    key128 = 0x51655468576D5A7133743677397A2443
    if secenek2=="1":
        cbc.cbc("AES",secenek3,key128,32)
    
    elif secenek2=="2":
        cfb.cfb("AES",secenek3,key128,32)
    
    elif secenek2=="3":
        ofb.ofb("AES",secenek3,key128,32)
    
    elif secenek2=="4":
        ctr.ctr("AES",secenek3,key128,32)
    
    
    """
    deneme=AES
    #master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    master_key = 0x72357538782F413F576E5A7234753778214125442A472D4B
    deneme.AES = AES(master_key)
    #plaintext = 0x53656c616d696e20616c65796b756d6d
    plaintext = hexoldu
    #plaintext=hex_value
    encrypted = deneme.AES.encrypt(plaintext)
    #ciphertext = 0x346eb9d37d8ded94725440cd80cff74b
    #ciphertext=0x45004b2cfb0f405488b6c968d27b8f3b
    decrypted = deneme.AES.decrypt(encrypted)
    """
elif secenek=="2" :
    key256=0x576D5A7133743677397A24432646294A404E635266556A586E32723575387821
    # Test vector for 128-bit key
    key128 = 0x51655468576D5A7133743677397A2443

    if secenek2=="1":
        cbc.cbc("CLEFIA",secenek3,key128,32)
    
    elif secenek2=="2":
        cfb.cfb("CLEFIA",secenek3,key128,32)
    
    elif secenek2=="3":
        ofb.ofb("CLEFIA",secenek3,key128,32)
    
    elif secenek2=="4":
        ctr.ctr("CLEFIA",secenek3,key128,32)
    
    #ctext1 = 0xa101c0deade330cf05f77a8b4b65c8dd
    #ctext256=0x8366070404b9786eecd2b8fec541c8d2
    #checkTestVector(key256,"SIZE_256",ptext,ctext256)
    #sifrelenmis=sifreleClefia(key128,"SIZE_128",ptext)
    #desifreleClefia(key128,"SIZE_128",sifrelenmis)
elif secenek=="3" :
    
    #text = 0xfedcba0987654321
    #text=0x28472B4B6250655368566D597133743677397A24432646294A404D635166546A576E5A7234753778214125442A472D4B6150645267556B58703273357638792F
    #KEY256
    #key = 0x6E3272357538782F413F4428472B4B6250655368566D59713373367639792442
    #key = 0x7638792F413F44287638792F413F4428
    """
    gostdeneme=gost.GOST()
    gostdeneme.set_key(key)
    sifrelenmis=gostdeneme.encrypt(text)
    gostdeneme.decrypt(sifrelenmis)
    """
    key128 = 0x51655468576D5A7133743677397A2443

    if secenek2=="1":
        cbc.cbc("GOST",secenek3,key128,16)
    
    elif secenek2=="2":
        cfb.cfb("GOST",secenek3,key128,16)
    
    elif secenek2=="3":
        ofb.ofb("GOST",secenek3,key128,16)
    
    elif secenek2=="4":
        ctr.ctr("GOST",secenek3,key128,16)
    
elif secenek=="4" :
    #hocanintext=0xfedcba0987654321fedcba0987654321
    #text=0xfedcba06fedcba06fedcba
    #text = 0xfedcba0987654321
    #text=0x28472B4B6250655368566D597133743677397A24432646294A404D635166546A576E5A7234753778214125442A472D4B6150645267556B58703273357638792F
    #KEY256
    #key = 0x6E3272357538782F413F4428472B4B6250655368566D59713373367639792442
    key64 = 0x7638792F413F4428 
    #key=0x576D5A7133743677397A24432646294A404E635266556A586E32723575387821
    #64 yazan text bit

    if secenek2=="1":
        cbc.cbc("KATAN",secenek3,key64,16)
    
    elif secenek2=="2":
        cfb.cfb("KATAN",secenek3,key64,16)
    
    elif secenek2=="3":
        ofb.ofb("KATAN",secenek3,key64,16)
    
    elif secenek2=="4":
        ctr.ctr("KATAN",secenek3,key64,16)
    #7025f283125442f3
elif secenek=="5" :
    hocanintext=0xfedcba0987654321
    text=0x7638792F413F4428 
    #text=0x28472B4B6250655368566D597133743677397A24432646294A404D635166546A576E5A7234753778214125442A472D4B6150645267556B58703273357638792F
    #KEY256
    #key = 0x6E3272357538782F413F4428472B4B6250655368566D59713373367639792442
    key64 = 0x7638792F413F4428  #64 bit
    #64 yazan text bit

    if secenek2=="1":
        cbc.cbc("KTANTAN",secenek3,key64,16)
    
    elif secenek2=="2":
        cfb.cfb("KTANTAN",secenek3,key64,16)
    
    elif secenek2=="3":
        ofb.ofb("KTANTAN",secenek3,key64,16)
    
    elif secenek2=="4":
        ctr.ctr("KTANTAN",secenek3,key64,16)