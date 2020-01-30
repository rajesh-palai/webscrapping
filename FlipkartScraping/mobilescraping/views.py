from django.shortcuts import render
from django.contrib import messages
from bs4 import BeautifulSoup
from django.conf import settings
import time
import requests
import csv
import urllib


def showmobile(request, item):
    file_name = "{}data.csv".format(settings.STATIC_URL)
    file = open(file_name, 'w')
    header = 'Name,Price,Url\n'
    file.write(header)

    url = "https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY".format(item)

    page_mobile = urllib.request.urlopen(url).read().decode('utf8', 'ignore')
    soup = BeautifulSoup(page_mobile, "lxml")
    products = soup.find_all("div", {"class": "_1UoZlX"})
    full_name = []
    full_price = []
    full_url = []
    for i in products:
        pdt_name = i.find('div', {'class': '_3wU53n'}).text
        link_name = i.find('a', {'class': '_31qSD5'})

        price = i.find('div', {'class': '_1vC4OE _2rQ-NK'}).text
        pdt_main_url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY' + link_name

        full_name.append(pdt_name)
        full_price.append(price)
        full_url.append(pdt_main_url)
        file.write(pdt_name + ',' + str(price) + ',' +  pdt_main_url + '\n')

    mylist = zip(full_name, full_price, full_url)
    file.close()
    return render(request, 'details.html', {'mylist': mylist})

