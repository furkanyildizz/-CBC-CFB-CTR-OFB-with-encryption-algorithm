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


def cbc(algoritmaIsmi,plaintext,key,ivboyut):
    print("")
    print("############################CCCCCCCCCCBBBBBBBBBBBCCCCCCCCCCC#########################")
    hexdigits = "0123456789ABCDEF"
    randomdigits = "".join([ hexdigits[random.randint(0,0xF)] for furkan  in range(ivboyut) ])
    iv = int(randomdigits, base=16)
    ivorj = int(randomdigits, base=16)
    print("ILK IV: ","%x" % iv)
    print("KEY: ","%x" % key)


    #################################################################################
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
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                print("GELEN TEXTIN PARCALARI: ",i)
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
            p1= iv ^ i
            print("IV ILE XORLANMIS HALI ENCRPYTE GIDECEK","%x" % p1)
            
            deneme=AES
            deneme.AES = AES(key)
            iv = deneme.AES.encrypt(p1)
            cipherlar.append(iv)
            print("SIRASI ILE CIKAN CIPHERLAR: ","%x" % iv)

        #decypt
        print("")
        print("---------DECRYPT KISMI---------")
        dizilen=-1*len(cipherlar)
        for i in range(dizilen+1,1):
           
            if len(cipherlar)==1:
                 deneme=AES
                 deneme.AES = AES(key)
                 di= deneme.AES.decrypt(cipherlar[-1*i-1])
                 plainim=ivorj ^ di 
                 plainler.append(plainim)
                 break

            
            deneme=AES
            deneme.AES = AES(key)
            di= deneme.AES.decrypt(cipherlar[-1*i])
            if -1*i==0:
               plainim=ivorj ^ di 
            else:
               plainim= cipherlar[(-1*i)-1]^ di

            plainler.append(plainim)
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))
            
    
#########################################################################CLEFIA#################
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
                hexlendi=i.encode("hex")
                sanane=(int(hexlendi, base=16)) 
                for j in range(0,eksik):
                    sanane = sanane*16
                print("GELEN TEXTIN PARCALARI: ",i)
                hexparcalanmisPlain.append(sanane)

        
        for i in hexparcalanmisPlain:
            print("GELEN TEXTIN PARCALARININ HEX HALI: ","%x" % i)
        #encrypt
        
        
        
        cipherlar=[]
        plainler=[]
        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
            p1= iv ^ i
            print("IV ILE XORLANMIS HALI","%x" % p1)

            iv =sifreleClefia(key,"SIZE_128",p1)
            cipherlar.append(iv)
            print("SIRASI ILE CIKAN CIPHERLAR: ","%x" % iv)

        #decypt
        print("")
        print("---------DECRYPT KISMI---------")
        dizilen=-1*len(cipherlar)
        for i in range(dizilen+1,1):
            """
            deneme=AES
            deneme.AES = AES(key)
            vi= deneme.AES.decrypt(iv)
            print("iiiiiiiiiiii","%x" % i)
            print("vvviiiiiiiiiiii","%x" % vi)
            iv= i ^ vi
            """
            if len(cipherlar)==1:
                 
                 di= desifreleClefia(key,"SIZE_128",(cipherlar[-1*i-1]))
                 plainim=ivorj ^ di 
                 plainler.append(plainim)
                 break

            
            
            di= desifreleClefia(key,"SIZE_128",(cipherlar[-1*i]))
            if -1*i==0:
               plainim=ivorj ^ di 
            else:
               plainim= cipherlar[(-1*i)-1]^ di

            plainler.append(plainim)
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))

    
###############################################################################GOST####################
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
       
        
        cipherlar=[]
        plainler=[]
        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
            p1= iv ^ i
            print("IV ILE XORLANMIS HALI","%x" % p1)
            gostdeneme.set_key(key)
            iv =gostdeneme.encrypt(p1)
            cipherlar.append(iv)
            print("SIRASI ILE CIKAN CIPHERLAR: ","%x" % iv)

        #decypt
        print("")
        print("---------DECRYPT KISMI---------")
        dizilen=-1*len(cipherlar)
        for i in range(dizilen+1,1):
            """
            deneme=AES
            deneme.AES = AES(key)
            vi= deneme.AES.decrypt(iv)
            print("iiiiiiiiiiii","%x" % i)
            print("vvviiiiiiiiiiii","%x" % vi)
            iv= i ^ vi
            """
            gostdeneme.set_key(key)
            if len(cipherlar)==1:
                 
                 di= gostdeneme.decrypt((cipherlar[-1*i-1]))
                 plainim=ivorj ^ di 
                 plainler.append(plainim)
                 break

            
            
            di= gostdeneme.decrypt((cipherlar[-1*i]))
            if -1*i==0:
               plainim=ivorj ^ di 
            else:
               plainim= cipherlar[(-1*i)-1]^ di

            plainler.append(plainim)
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))
            
    ############################################################################

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
        ####encrypt
        
        katandeneme=katan.KATAN(key,64)
       
        
        cipherlar=[]
        plainler=[]
        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
            p1= iv ^ i
            print("IV ILE XORLANMIS HALI","%x" % p1)
            
            iv =katandeneme.enc(p1)
            cipherlar.append(iv)
            print("SIRASI ILE CIKAN CIPHERLAR: ","%x" % iv)

        #decypt
        print("")
        print("---------DECRYPT KISMI---------")
        dizilen=-1*len(cipherlar)
        for i in range(dizilen+1,1):
            """
            deneme=AES
            deneme.AES = AES(key)
            vi= deneme.AES.decrypt(iv)
            print("iiiiiiiiiiii","%x" % i)
            print("vvviiiiiiiiiiii","%x" % vi)
            iv= i ^ vi
            """
            
            if len(cipherlar)==1:
                 
                 di= katandeneme.dec((cipherlar[-1*i-1]))
                 plainim=ivorj ^ di 
                 plainler.append(plainim)
                 break

            
            
            di= katandeneme.dec((cipherlar[-1*i]))
            if -1*i==0:
               plainim=ivorj ^ di 
            else:
               plainim= cipherlar[(-1*i)-1]^ di

            plainler.append(plainim)
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))
    ########################################################################

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
        ####encrypt
        
        ktantandeneme=ktantan.KTANTAN(key,64)

        cipherlar=[]
        plainler=[]
        for i in hexparcalanmisPlain:
            print(" ")
            print("TEXTIN YALIN HALI","%x" % i)
            p1= iv ^ i
            print("IV ILE XORLANMIS HALI","%x" % p1)
            
            iv =ktantandeneme.enc(p1)
            cipherlar.append(iv)
            print("SIRASI ILE CIKAN CIPHERLAR: ","%x" % iv)

        #decypt
        print("")
        print("---------DECRYPT KISMI---------")
        dizilen=-1*len(cipherlar)
        for i in range(dizilen+1,1):
            """
            deneme=AES
            deneme.AES = AES(key)
            vi= deneme.AES.decrypt(iv)
            print("iiiiiiiiiiii","%x" % i)
            print("vvviiiiiiiiiiii","%x" % vi)
            iv= i ^ vi
            """
            
            if len(cipherlar)==1:
                 
                 di= ktantandeneme.dec((cipherlar[-1*i-1]))
                 plainim=ivorj ^ di 
                 plainler.append(plainim)
                 break

            
            
            di= ktantandeneme.dec((cipherlar[-1*i]))
            if -1*i==0:
               plainim=ivorj ^ di 
            else:
               plainim= cipherlar[(-1*i)-1]^ di

            plainler.append(plainim)
        
        for i in plainler:
            print("PLAINLER BULUNDU HEX: ","%x" % i)
            print("PLAINLER BULUND TEXT: ",convert_hex_to_ascii(i))
            
            