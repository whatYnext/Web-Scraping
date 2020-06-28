# -*- coding: utf-8 -*-
"""
Web scraping on BaiDubaike. 
1. Set a first page, then random find website in it.
2. Run it for fixed times to see where you got the website.

@author: mayao
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import error
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]
    try:
        html = urlopen(url).read().decode('utf-8')
    except error.URLError:  #IF invalid website, ignore and restart again 
        his.pop()
        his.append(random.sample(sub_urls, 1)[0]['href'])
        continue
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()
