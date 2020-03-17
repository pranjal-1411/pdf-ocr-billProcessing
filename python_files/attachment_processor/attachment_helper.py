import datetime
from datetime import date

def processAttachment( downloadUrl , fileType ):
    dateObject =  datetime.datetime.strptime( '12/02/2020' , '%d/%m/%Y')
    return { 'amount':{ 'unit':'INR','value':'12'},'date': dateObject , 'category':'Food' }

    