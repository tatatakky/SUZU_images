# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib.request

try:
    os.mkdir('SUZU_images_all')

except OSError:
    print('already exists')

count = 0

for p in [1,2,3,4]:
    url = 'https://matome.naver.jp/odai/2148553130456013901?&page=' + str(p)

    suzu_data = requests.get(url)
    soup = BeautifulSoup(suzu_data.text,'html.parser')

    def download_image(url, count):
        full_name = str(count) + ".jpg"
        urllib.request.urlretrieve(url, full_name)

    for i in soup.findAll("div",{'class','mdMTMWidget01ItemImg01'}):
        for j in i.findAll("p",class_ = "mdMTMWidget01ItemImg01View"):
            for x in j.findAll("a"):
                for y in x.findAll("img"):
                    suzu_images = y.get('src')
                    print(suzu_images)
                    download_image(suzu_images,count)
                    count+=1

cmd = 'mv *.jpg ./SUZU_images_all'
os.system(cmd)
