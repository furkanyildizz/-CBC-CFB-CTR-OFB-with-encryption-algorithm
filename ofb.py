import unittest
from aes import AES
from clefia import sifreleClefia
from clefia import desifreleClefia
import gost
import katan
import ktantan
import random

def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)


def ofb(algoritmaIsmi,plaintext,key,ivboyut):
    print("")
    print("####################OFB#####################")
    hexdigits = "0123456789ABCDEF"
    randomdigits = "".join([ hexdigits[random.randint(0,0xF)] for furkan  in range(ivboyut) ])
    iv = int(randomdigits, base=16)
    ivorj = int(randomdigits, base=16)
    print("ILK IV: ","%x" % iv)
    print("KEY: ","%x" % key)
#############################################"AES"############################################################
    if algoritmaIsmi=="AES":
        parcalaPlain=[]
        hexparcalanmisPlain=[]
        parcalaPlain=list(plaintext)
        sayac=0
        bosstring=""
        parcalanmisPlain=[]
        for i in parcalaPlain:
            bosstring=bosstring+str(i)
            sayac=sayac+1
            if sayac % 16 ==0:
                parcalanmisPlain.append(bosstring)
                bosstring=""

        parcalanmisPlain.append(bosstring)
        bosstring=""
    
        for i in parcalanmisPlain:
            #print(len(i))
            if len(i)==16:
                hexlendi=i.encode("hex")
                hexparcalanmisPlain.append(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
            elif len(i)!=0:
                eksik=32-(len(i)*2)
                print("GELEN TEXTIN PARCALARI: ",i)
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        
        cipherlar=[]
        plainler=[]

        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
            deneme=AES
            deneme.AES = AES(key)
            vi = deneme.AES.encrypt(iv)
            cipher=vi ^ i
            cipherlar.append(cipher)
            print("PLAIN VE ENCRYPTDEN CIKAN IV ILE XORLANMIS CIPHERLAR: ","%x" % cipher)
            iv=vi
        #DECRYPT
        print("")
        print("---------DECRYPT KISMI---------")
        for i in cipherlar:
            
            deneme=AES
            deneme.AES = AES(key)
            vi = deneme.AES.encrypt(ivorj)
            plain=vi ^ i
            print("CIPHER ILE XORLARMIS PLAIN","%x" % plain)
            plainler.append(plain)
            ivorj=vi
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

########################################################CLEFIA###########################################
    if algoritmaIsmi=="CLEFIA":
        parcalaPlain=[]
        hexparcalanmisPlain=[]
        parcalaPlain=list(plaintext)
        sayac=0
        bosstring=""
        parcalanmisPlain=[]
        for i in parcalaPlain:
            bosstring=bosstring+str(i)
            sayac=sayac+1
            if sayac % 16 ==0:
                parcalanmisPlain.append(bosstring)
                bosstring=""

        parcalanmisPlain.append(bosstring)
        bosstring=""
    
        for i in parcalanmisPlain:
            #print(len(i))
            if len(i)==16:
                hexlendi=i.encode("hex")
                hexparcalanmisPlain.append(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
            elif len(i)!=0:
                eksik=32-(len(i)*2)
                print("GELEN TEXTIN PARCALARI: ",i)
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        
        cipherlar=[]
        plainler=[]

        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
    
            vi = sifreleClefia(key,"SIZE_128",iv)
            cipher=vi ^ i
            cipherlar.append(cipher)
            print("PLAIN VE ENCRYPTDEN CIKAN IV ILE XORLANMIS CIPHERLAR: ","%x" % cipher)
            iv=vi
        
        #DECRYPT
        print("")
        print("---------DECRYPT KISMI---------")
        for i in cipherlar:
            
            vi = sifreleClefia(key,"SIZE_128",ivorj)
            plain=vi ^ i
            print("CIPHER ILE XORLARMIS PLAIN","%x" % plain)
            plainler.append(plain)
            ivorj=vi
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

    
###################################################GOST##############################################
    if algoritmaIsmi=="GOST":
        parcalaPlain=[]
        hexparcalanmisPlain=[]
        parcalaPlain=list(plaintext)
        sayac=0
        bosstring=""
        parcalanmisPlain=[]
        for i in parcalaPlain:
            bosstring=bosstring+str(i)
            sayac=sayac+1
            if sayac % 8 ==0:
                parcalanmisPlain.append(bosstring)
                bosstring=""

        parcalanmisPlain.append(bosstring)
        bosstring=""
    
        for i in parcalanmisPlain:
            #print(len(i))
            if len(i)==8:
                hexlendi=i.encode("hex")
                hexparcalanmisPlain.append(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
            elif len(i)!=0:
                eksik=16-(len(i)*2)
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                print("GELEN TEXTIN PARCALARI: ",i)
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        gostdeneme=gost.GOST()
        gostdeneme.set_key(key)
        cipherlar=[]
        plainler=[]

        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
    
            vi = gostdeneme.encrypt(iv)
            cipher=vi ^ i
            cipherlar.append(cipher)
            print("PLAIN VE ENCRYPTDEN CIKAN IV ILE XORLANMIS CIPHERLAR: ","%x" % cipher)
            iv=vi
        
        #DECRYPT
        print("")
        print("---------DECRYPT KISMI---------")
        for i in cipherlar:
            
            vi = gostdeneme.encrypt(ivorj)
            plain=vi ^ i
            print("CIPHER ILE XORLARMIS PLAIN","%x" % plain)
            plainler.append(plain)
            ivorj=vi
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

#########################################KATAN#################################################
    if algoritmaIsmi=="KATAN":
        parcalaPlain=[]
        hexparcalanmisPlain=[]
        parcalaPlain=list(plaintext)
        sayac=0
        bosstring=""
        parcalanmisPlain=[]
        for i in parcalaPlain:
            bosstring=bosstring+str(i)
            sayac=sayac+1
            if sayac % 8 ==0:
                parcalanmisPlain.append(bosstring)
                bosstring=""

        parcalanmisPlain.append(bosstring)
        bosstring=""
    
        for i in parcalanmisPlain:
            #print(len(i))
            if len(i)==8:
                hexlendi=i.encode("hex")
                hexparcalanmisPlain.append(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
            elif len(i)!=0:
                eksik=16-(len(i)*2)
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                print("GELEN TEXTIN PARCALARI: ",i)
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        katandeneme=katan.KATAN(key,64)
        cipherlar=[]
        plainler=[]

        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
    
            vi = katandeneme.enc(iv)
            cipher=vi ^ i
            cipherlar.append(cipher)
            print("PLAIN VE ENCRYPTDEN CIKAN IV ILE XORLANMIS CIPHERLAR: ","%x" % cipher)
            iv=vi
        
        #DECRYPT
        print("")
        print("---------DECRYPT KISMI---------")
        for i in cipherlar:
            
            vi = katandeneme.enc(ivorj)
            plain=vi ^ i
            print("CIPHER ILE XORLARMIS PLAIN","%x" % plain)
            plainler.append(plain)
            ivorj=vi
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

#############################################KTANTAN######################################

    if algoritmaIsmi=="KTANTAN":
        parcalaPlain=[]
        hexparcalanmisPlain=[]
        parcalaPlain=list(plaintext)
        sayac=0
        bosstring=""
        parcalanmisPlain=[]
        for i in parcalaPlain:
            bosstring=bosstring+str(i)
            sayac=sayac+1
            if sayac % 8 ==0:
                parcalanmisPlain.append(bosstring)
                bosstring=""

        parcalanmisPlain.append(bosstring)
        bosstring=""
    
        for i in parcalanmisPlain:
            #print(len(i))
            if len(i)==8:
                hexlendi=i.encode("hex")
                hexparcalanmisPlain.append(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
            elif len(i)!=0:
                eksik=16-(len(i)*2)
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                print("GELEN TEXTIN PARCALARI: ",i)
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        ktantandeneme=ktantan.KTANTAN(key,64)
        cipherlar=[]
        plainler=[]

        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
    
            vi = ktantandeneme.enc(iv)
            cipher=vi ^ i
            cipherlar.append(cipher)
            print("PLAIN VE ENCRYPTDEN CIKAN IV ILE XORLANMIS CIPHERLAR: ","%x" % cipher)
            iv=vi
        
        #DECRYPT
        print("")
        print("---------DECRYPT KISMI---------")
        for i in cipherlar:
            
            vi = ktantandeneme.enc(ivorj)
            plain=vi ^ i
            print("CIPHER ILE XORLARMIS PLAIN","%x" % plain)
            plainler.append(plain)
            ivorj=vi
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

