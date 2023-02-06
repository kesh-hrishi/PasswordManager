from getpass import getpass
from dbconnet import dbconfig
from rich import print as printc
from rich.console import Console
import string
import hashlib
import random

console= Console()



def configure():
    db=dbconfig()
    curr=db.cursor()


    curr.execute("SELECT * FROM pmsecrets")
    print(curr.fetchall())





















    """
    querry="CREATE TABLE pmsecrets (masterpassword TEXT NOT NULL, device_secret TEXT NOT NULL)"
    try:
        res=curr.execute(querry)
        printc("[green][+][/green] Table 'secrets' created")
    except Exception as e:
        console.print_exception(show_locals=True)
    """
        

configure()