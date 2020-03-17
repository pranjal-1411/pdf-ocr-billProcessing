import datetime
from datetime import date
import python_files.attachment_processor.extractText as textExtractor
import python_files.attachment_processor.getAmount as amountFinder
import python_files.attachment_processor.getDate as dateFinder
import python_files.attachment_processor.getCategory as categoryFinder 

# returns data = { 'amount':{ 'unit':'INR','value':'12'},'date': dateObject , 'category':'Food' }
def processAttachment( downloadUrl , fileType ):
    
    extractTextPath = textExtractor.downloadFile( downloadUrl, fileType )
    if extractTextPath is None:
        print('Error in downloading')
        return None 
    amount = amountFinder.getAmount( extractTextPath )
    date = dateFinder.getDate( extractTextPath )
    category = categoryFinder.getCategory( extractTextPath )
    
    data = { 'amount': { 'unit':'INR','value':amount } , 'date':date , 'category':category }
    print(data)
    return data

if __name__ == "__main__":
    processAttachment( 'sds','sdf' )   