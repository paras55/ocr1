from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os 
import tempfile
 
PDF_file = "python.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#pages = convert_from_path(PDF_file, 500) 



path=r'C:\Users\dell\Desktop\Scripts\thapar\research_electron-master\web_app\flask_app_latest'
with tempfile.TemporaryDirectory() as path:
    pages= convert_from_path(PDF_file)
    image_counter = 0
    outfile = "out1_text.txt"
    
    
    f = open(outfile, "a", encoding="utf-8") 
    
    for page in pages: 	
        filename = "page_"+str(image_counter)+".jpg"	
        page.save(filename, 'JPEG') 	
        image_counter = image_counter + 1
        text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    
    	
        text = text.replace('-\n', '')	 
    
    	 
        f.write(text) 
        os.unlink(filename)
    
    
    f.close()
