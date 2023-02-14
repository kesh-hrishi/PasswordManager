from dbconnet import dbconfig
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from rich import print as printc

import aesutil


def getmasterkey(mp,ds):
    password=mp.encode()
    salt=ds.encode()
    key=PBKDF2(password,salt,32,count=1000000,hmac_hash_module=SHA512)
    return key


def addEntry(mp,ds,sitename,siteurl,email,username):
    password=getpass("Password:")
        
    mk=getmasterkey(mp,ds)
    
    
    encrypted=aesutil.encrypt(key=mk,source=password,keyType="bytes")
    
    

    db=dbconfig()
    curr=db.cursor()

    querry="INSERT INTO pmmain(sitename,siteurl,email,username,password) VALUES (%s, %s, %s, %s, %s)"
    val=(sitename,siteurl,email,username,encrypted)
    curr.execute(querry, val)
    db.commit()

    printc("[green] Added entry")

