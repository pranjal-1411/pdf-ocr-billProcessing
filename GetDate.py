import re
import datetime
from datetime import date
from dateutil.parser import parse

def GetDate(inFile):

    extractedDate = extractDate(inFile)
    if extractedDate == -1 :  
        dateObject = findDate(inFile) #if GetDate does not work then we will check with findDate
        if dateObject == None : return None
        return dateObject.date()
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

'''
    NOTE :  findDate will find the date if the representation of the date is like "6 jul, 2019"
'''
def findDate(inFile):
    f = open(inFile, "r")
    ans = None
    for line in f:
            try :
               ans = parse(line, fuzzy_with_tokens=True)
               break
            except Exception:
                pass        
    f.close()
    if ans == None:
        return ans
    print(ans[0])
    return ans[0]

if __name__ == "__main__":       
    GetDate('out_text.txt')

