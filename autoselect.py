# -*- -*-
#http://www.lfd.uci.edu/~gohlke/pythonlibs/
#sudo apt-get install tesseract-ocr
#pip install PIL 
#pip install pytesseract

import os
from PIL import Image
from pytesser import *
#import cStringIO
import requests
import shutil
import re

script_dir = os.path.dirname(os.path.abspath(__file__))

logincheck_header= {
'Proxy-Connection' : 'keep-alive' ,
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2288.6 Safari/537.36',
'DNT' : '1',
'Referer' : 'http://cos4.ntnu.edu.tw/AasEnrollStudent/',
'Accept-Encoding' : 'gzip, deflate, sdch' ,
'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4'
}

login_header= {
'Proxy-Connection': 'keep-alive' ,
'Origin': 'http://cos4.ntnu.edu.tw' ,
'X-Requested-With': 'XMLHttpRequest' ,
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2288.6 Safari/537.36' ,
'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8' ,
'Accept': '*/*' ,
'DNT' : '1' ,
'Referer' : 'http://cos4.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW' ,
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4'
}


userid = '40040001S'
password = 'XDDDDDDDD'




logincheck_url = 'http://cos4.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW'
response = requests.get(logincheck_url, headers=logincheck_header)
JSESSIONID = response.cookies['JSESSIONID']
print "cookies :" + JSESSIONID

m = re.search(r'url:\'LoginCheckCtrl\?action=login&id=\' \+ \'([0-9a-zA-Z]+)\',' , response.content)
login_id = m.group(1)
print "id : " + login_id

Captcha_url = 'http://cos4.ntnu.edu.tw/AasEnrollStudent/RandImage'
Captcha_res = requests.get(Captcha_url, stream=True)
with open(os.path.join(script_dir, 'img'), 'wb') as out_file:
    shutil.copyfileobj( Captcha_res.raw, out_file )
out_file.close
del Captcha_res
#img_file = cStringIO.StringIO(response.read())   
#image = Image.open(img_file)
#image = Image.open("C:/Users/Andy/git_repo/a/fnord.tif")
#image = Image.open( open("~/auto_s/fnord.tif", 'rb'))
#import os.path

#script_dir = os.path.dirname(os.path.abspath(__file__))
print script_dir
image = Image.open(os.path.join(script_dir, 'img'))

	


#image = Image.open( r"./img")



Captcha_code = image_to_string(image).strip()
print "Captcha_code:" + Captcha_code
#a = image_file_to_string('img')
#print type(a)


login_header['Cookie'] = 'JSESSIONID=' + JSESSIONID 
print login_header

login_payload = {'userid': userid , 'password': password , 'validateCode' : Captcha_code , 'checkTW' : '1' }
print login_payload



login_url = 'http://cos4.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?action=login&id='+login_id


response = requests.post(login_url, data=login_payload ,headers=login_header)
print "======================"
print response.status_code
print response.headers
print response
#q = 
#print response.json()
print response.text
print response.content
print "======================"