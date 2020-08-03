#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:07:43 2020

@author: maggiezhang
"""

# Creating a python script to atuomatically notify me when prices drop on my favorite clothing/jewelry

import requests as r
import time
import schedule
from bs4 import BeautifulSoup

sites = ["https://takenaka-global.com/collections/bento-box-rectangle/products/bento-box-rectangle-pistachio-green"]#"https://mejuri.com/shop/products/thin-croissant-dome-ring"] 
             #"https://kinnstudio.com/collections/necklaces/products/alphabet-charm-pendant",
             #"https://takenaka-global.com/collections/bento-box-rectangle/products/bento-box-rectangle-pistachio-green",
             #"https://www.everlane.com/products/womens-day-boot-reknit-slate-grey?collection=womens-shoes-accessories"
             #]
prices = [0]*len(sites)

def task():
    for s in sites:
        html = r.get(s).text
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        box = soup.find('span', attrs={'class': 'money'})
        print(box.children)
        for i in box: print(i)
        ring = soup.find("meta",  property="product:price:amount")
        price = (ring["content"] if ring else "free?")
        
    
task()
schedule.every().hour.do(task)

'''
while True:
    schedule.run_pending()
    time.sleep(60*60)
'''
