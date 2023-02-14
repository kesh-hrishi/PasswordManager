import psycopg2
from rich import print as printc
from rich.console import Console
console= Console()

def dbconfig():    
        try:
                conn=psycopg2.connect(host="awsdatapassword.ceqpb6xxp8dr.ap-south-1.rds.amazonaws.com",dbname="passworddatabase",user="postgres",password="hrishikesh")
                
                    
        except Exception as e:
                console.print_exception(show_locals=True)
    
        return conn
    



    
