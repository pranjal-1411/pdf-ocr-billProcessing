import re

def GetAmount(inFile):

    f = open(inFile,"r")
    Amount = "((([0-9]+)\.([0-9]+))|([0-9]+))"
    ans = '-1'
    for line in f:
        x = re.search(Amount, line)
        if x and findPattern(line)  :
            ans = x.group()
            print(ans)
    #print(ans)
    f.close()

def findPattern( line ):
    
    if line.find('Total') !=-1 : return True 
    # Add other such statements
    return False; 

GetAmount("out_text.txt")