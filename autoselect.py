#http://www.lfd.uci.edu/~gohlke/pythonlibs/
#sudo apt-get install tesseract-ocr
#pip install PIL 
#pip install pytesseract

import os
from PIL import Image
from pytesser import *
import cStringIO
import requests
import shutil

url = 'http://cos4.ntnu.edu.tw/AasEnrollStudent/RandImage'

response = requests.get(url, stream=True)
#image = response.raw

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, 'img'), 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
out_file.close

del response
#img_file = cStringIO.StringIO(response.read())   
#image = Image.open(img_file)
#image = Image.open("C:/Users/Andy/git_repo/a/fnord.tif")
#image = Image.open( open("~/auto_s/fnord.tif", 'rb'))
#import os.path

#script_dir = os.path.dirname(os.path.abspath(__file__))
print script_dir
image = Image.open(os.path.join(script_dir, 'img'))

	


#image = Image.open( r"./img")



auth_code = image_to_string(image)
print auth_code
#a = image_file_to_string('img')
#print type(a)