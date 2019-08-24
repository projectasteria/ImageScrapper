import http.cookiejar
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

import requests
from bs4 import BeautifulSoup

def get_soup(url, header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), 'html.parser')

def download_images(query, project_name):
    image_type = "Image"
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q={}&tbm=isch&source=lnt&tbs=isz:m".format(query)
    DIR = "Project/{}".format(project_name)
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url, header)

    ActualImages = [] 
    for a in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link, Type))

    print("there are total", len(ActualImages), "images")

    if not os.path.exists(DIR):
        os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
        os.mkdir(DIR)
    for i, (img, Type) in enumerate(ActualImages):
        try:
            raw_img = requests.get(img, headers=header).content
            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            if len(Type) == 0:
                f = open(os.path.join(DIR, image_type + "_" + str(cntr)+".jpg"), 'wb')
            else:
                f = open(os.path.join(DIR, image_type + "_" + str(cntr)+"."+Type), 'wb')
            f.write(raw_img)
            f.close()
        
        except Exception as e:
            print("could not load : "+img)
            print(e)
