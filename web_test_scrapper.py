import os
from bs4 import BeautifulSoup
import requests





url_test = "http://127.0.0.1/shameit"

re = requests.get(url_test)
st = re.text
soup = BeautifulSoup(st, "html.parser")
title = soup.find_all("title")

f = open("t.txt", "w+")
f.write(str(title[0]))
f.close()


