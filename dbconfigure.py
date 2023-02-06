
from getpass import getpass
from dbconnet import dbconfig
from rich import print as printc
from rich.console import Console
import string
import hashlib
import random

console= Console()



def GenerateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))




def configure():
    db=dbconfig()
    curr=db.cursor()

    
    curr.execute("CREATE TABLE pmsecrets (masterpassword TEXT NOT NULL, device_secret TEXT NOT NULL);")
    print("TABLE 'pmsecrets' CREATED")
    
    curr.execute("CREATE TABLE pmmain (websitename TEXT NOT NULL, websiteurl TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL);")
    print("TABLE 'pmmain' CREATED")
    
    db.commit()

    count=3
    masterpassword=""
    while count>=1:
        masterpassword=getpass("Choose a masterpassword:")
        if masterpassword==getpass("retype the password:") and masterpassword != "":
            printc("[green]MASSTER PASSWORD SET\n")
            break         
        else:
            count -= 1
            printc("[red][!] PASSWORD DOESN'T MATCH TRY AGAIN (attempts left:",count,"[red])\n")

    hashed_masterpass=hashlib.sha256(masterpassword.encode()).hexdigest()
    printc("[green]GENERATED HASH OF THE MASTERPASSWORD\n")
                            
    ds=GenerateDeviceSecret()
    printc("[green]GENERATED DEVICE SECRET\n")

    querry="INSERT INTO pmsecrets (masterpassword , device_secret) values(%s, %s);"
    value=(hashed_masterpass,ds)
    curr.execute(querry,value)
    db.commit()
    printc("[green]Added details to the database")
    printc("[green]CONFIGURATION COMPLETE")

    db.close()

        
configure()   
    




