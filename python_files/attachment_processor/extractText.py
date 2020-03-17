import requests 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os

# toDo    return extracted file path address from this function
def downloadFile( fileUrl , extension ):
    r = requests.get(fileUrl) # create HTTP response object 
    imagePathList = []
    if(extension == "file" ):
        with open("downloadFile.pdf",'wb') as f: 
            f.write(r.content)
       
        pages = convert_from_path("./downloadFile.pdf") 
        image_counter = 1
        for page in pages: 
            filename = "page_"+str(image_counter)+".jpg"
            imagePathList.append(filename)
            page.save(filename, 'JPEG') 
            image_counter = image_counter + 1

    elif(extension == "image"):
        with open("downloadFile.jpg",'wb') as f: 
            f.write(r.content)
        imagePathList.append("downloadFile.jpg")
    
    generateTextFile( imagePathList )
    return "out_text.txt" 

def generateTextFile( imagePathList) :
            
    outfile = "out_text.txt"
    f = open(outfile, "w") 
    for path in imagePathList:
        text = str(((pytesseract.image_to_string(Image.open(path).convert("LA"))))) 
        text = text.replace('-\n', '')      
        f.write(text) 
           

if __name__ == "__main__":
    imagePathList = []    
    pages = convert_from_path("./bill3.pdf") 
    image_counter = 1
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        imagePathList.append(filename)
        page.save(filename, 'JPEG') 
        image_counter = image_counter + 1   
    generateTextFile(imagePathList)


 
