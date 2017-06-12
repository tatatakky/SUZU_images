# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib.request

suzu_data = requests.get("https://matome.naver.jp/odai/2148553130456013901")
soup = BeautifulSoup(suzu_data.text,'html.parser')

try:
    os.mkdir('SUZU_images')
except OSError:
    print('already exists')

count = 0
#sen = ""

def download_image(url, count):
    full_name = str(count) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

for i in soup.findAll("div",{'class','mdMTMWidget01ItemImg01'}):
    for j in i.findAll("p",class_ = "mdMTMWidget01ItemImg01View"):
        for x in j.findAll("a"):
            for y in x.findAll("img"):
                suzu_images = y.get('src')
                print(suzu_images)
#                print(sen)
                download_image(suzu_images,count)
                count+=1
#                os.system('clear')
#                sen = sen + "-"
#print(sen)
cmd = 'mv *.jpg ./SUZU_images'
os.system(cmd)
