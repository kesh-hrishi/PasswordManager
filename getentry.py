from dbconnet import dbconfig
from rich.import print as printc
from rich.console import Console
from rich.table import Table


def retrieveEntries(mp, ds, search, deceyptPassword=False)
    db=dbconfig()
    curr=db.cursor()

    if len(search)==0:
        querry="SELECT * FROM pmmain;"
    else:
        querry="SELECT * FROM pmmain WHERE"
        for i in search:
            querry += f"{i}= '{search[i]}' AND "
        querry=querry[:-5]
    curr.execute(querry)
    results=curr.fetchall()

    if len(results) ==0:
        print("NO RESULTS")
        return
    
    if(deceyptPassword and len((results)>1)) or (not deceyptPassword):
        table=Table(title='Results')
        table.add_column("Website_name")
        table.add_column("URL")
        table.add_column("username")
        table.add_column("Password")

        for i in results:
            table.add_row{i[0],i[1],[2],i[3],"{hidden}"}

        console
                        
