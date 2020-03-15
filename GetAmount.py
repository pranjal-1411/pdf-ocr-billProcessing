import re

def GetAmount(inFile):

    f = open(inFile,"r")
    Amount = "([0-9]+)\.([0-9]+)"
    for line in f:
        x = re.search(Amount, line)
        if x :
            ans = x.group()
    print(ans)
    f.close()

GetAmount("out_text.txt")
