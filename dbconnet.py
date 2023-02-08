import psycopg2
from rich import print as printc
from rich.console import Console
console= Console()

def dbconfig():    
        try:
                conn=psycopg2.connect( dbname="passworddatabase", user="postgres",password="!l@vegu!t@r")
                
                    
        except Exception as e:
                console.print_exception(show_locals=True)
    
        return conn
    



    
