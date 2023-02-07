from dbconnet import dbconfig
from rich import print as printc
from rich.console import Console
from rich.table import Table
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import aesutil
import pyperclip


def getmasterkey(mp,ds):
    password=mp.encode()
    salt=ds.encode()
    key=PBKDF2(password,salt,32,count=1000000,hmac_hash_module=SHA512)
    return key

def retrieveEntries(mp, ds, search, decryptPassword=False):
    db=dbconfig()
    curr=db.cursor()

    querry=""

    if len(search)==0:
        querry="SELECT * FROM pmmain"
    else:
        querry="SELECT * FROM pmmain WHERE"
        for i in search:
            querry+= f"{i} = '{search[i]}' AND "
        querry = querry[: -5]
    
    curr.execute(querry)
    results=curr.fetchall()

    if len(results) == 0:
        printc("[yellow] No results")
        return
    
    if(decryptPassword and len(results)>1 or (not decryptPassword)):
        table=Table(title="Results")
        table.add_column("Site Name")
        table.add_column("Url")
        table.add_column("Email")
        table.add_column("Username")
        table.add_column("Password")

        for i in results:
            table.add_row(i[0],i[1],i[2],i[3],"{hidden}")
        
        console=Console()
        console.print(table)

        return
    
    if len(results)==1 and decryptPassword:
        mk=getmasterkey(mp,ds)
        decrypted=aesutil.decrypt(key=mk, source=results[0][4], keyType="bytes")

        pyperclip.copy(decrypted.decode())
        printc("[green] PASSWORD COPIED TO CLIPBOARD")

    db.close()



