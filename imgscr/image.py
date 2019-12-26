#fake user agent for forbiding clorer
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}

#scrayping function
#requests.get(url, header(uafake))
import requests
def download_data(url):
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		return response.content
	else:
		print('false:', response.status_code)

import traceback
def save_file(data, file_name):
	try:
		with open(file_name, 'wb') as f:
			f.write(data)
	except:
		print('failed for saving data')
		traceback.print_exc()


import urllib.request, urllib.error
from bs4 import BeautifulSoup

#setting url
u = input('url:')
f = open('setting','w')
f.write(u)
f.close()

f = open('setting')
url = f.read()
f.close()

#setting classname
import re
request = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(request)
soup = BeautifulSoup(html, "html.parser")
#elm2 = soup.find_all('img', class_=re.compile('alignnone'))
#elm2 = soup.find_all('img', class_=re.compile('content-img'))
#elm2 = soup.find_all('img', src=re.compile('1486'))
elm2 = soup.find_all('img', src=re.compile('521'))

num = 0
for i in elm2:
	num+=1
	imgname = str(num) + ".jpg"
	print(i.attrs['src'])
	print(imgname)
	data = download_data(i.attrs['src'])
	save_file(data, imgname)

#make folder, mv jpg
import os
p = '/var/www/html/ぜつりんこ/webapi/public/contents/'
foldername = input('foldername:')
path = p + foldername
os.makedirs(path)

import shutil
import glob
l = glob.glob('*.jpg')
for i in l:
	shutil.move(i, path)
