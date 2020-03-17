import re
import datetime
from datetime import date

def getDate(inFile):

    extractedDate = extractDate(inFile)
    if extractedDate == None : return None 
    
    dateObject = None
   
    if re.search(r'\d{2}/\d{2}/\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d/%m/%Y')
    elif re.search(r'\d{4}/\d{2}/\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y/%m/%d')
    elif re.search(r'\d{4}-\d{2}-\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y-%m-%d')
    elif re.search(r'\d{2}-\d{2}-\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d-%m-%Y') 
    
    if dateObject is None : return None
    return str(dateObject.date())
    

def extractDate( inFile ):

    f = open(inFile,"r")
    DatePattern = "((\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})|(\d{4}-\d{2}-\d{2})|(\d{2}-\d{2}-\d{4}))"
    ans = None
    for line in f:
       # print(line)
        x = re.search(DatePattern, line)
        if x :
            print(line)
            ans = x.group()
            print(ans)
            break 
    f.close()
    return ans

if __name__ == "__main__":       
    getDate('out_text.txt')
     
    