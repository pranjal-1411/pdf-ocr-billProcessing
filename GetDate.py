import re
import datetime
from datetime import date

def GetDate(inFile):

    extractedDate = extractDate(inFile)
    if extractedDate == -1 : return None 
    dateObject = None
 
    if re.search(r'\d{2}/\d{2}/\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d/%m/%Y')
    elif re.search(r'\d{4}/\d{2}/\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y/%m/%d')
    elif re.search(r'\d{4}-\d{2}-\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y-%m-%d')
    elif re.search(r'\d{2}-\d{2}-\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d-%m-%Y') 
    print(dateObject.date())
    return dateObject.date()
    

def extractDate( inFile ):

    f = open(inFile,"r")
    DatePattern = "((\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})|(\d{4}-\d{2}-\d{2})|(\d{2}-\d{2}-\d{4}))"
    ans = -1
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
    GetDate('out_text.txt')
     
    