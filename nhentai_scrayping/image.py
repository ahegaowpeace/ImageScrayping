########################################################################
#				mkdir & cd			       #
########################################################################
import os
import sys
import shutil
p = './contents/'
foldername = sys.argv[1]
path = p + foldername
os.makedirs(path)
os.chdir(path)


#fake user agent for forbiding clorer
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}

#scrayping function
#requests.get(url, header(uafake))
import requests
def download_data(url):
	#response = requests.get(url,headers=headers)
	response = requests.get(url,headers=headers, timeout=(None, None))
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

##########################################################################
#				target url                               #
##########################################################################
num = 0

##########################################################################
#			range:1 to last page + 1                         #
#		sample:https://nhentai.net/g/272740/                     #
##########################################################################
u = sys.argv[2]
u = u[:-2]
n = int(sys.argv[3])

for nm in range(1,int(n) + 1): 
	url = u
	url2 = url + str(nm) + "/"
	print(url2)

	#setting classname
	import re
	request = urllib.request.Request(url=url2, headers=headers)
	html = urllib.request.urlopen(request)
	soup = BeautifulSoup(html, "html.parser")
	#elm2 = soup.find_all('img', class_=re.compile('alignnone'))
	#elm2 = soup.find_all('img', class_=re.compile('content-img'))
	elm2 = soup.find_all('img', src=re.compile('i.nhentai.net/galleries'))
	#elm2 = soup.find_all('img', src=re.compile('521'))
	#elm2 = soup.find_all('img', src=re.compile('qTX7sdgw3U'))
	
	for i in elm2:
		num+=1
		imgname = str(num) + ".jpg"
		print(i.attrs['src'])
		print(imgname)
		data = download_data(i.attrs['src'])
		save_file(data, imgname)
