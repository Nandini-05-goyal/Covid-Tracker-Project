# important imports
from bs4 import BeautifulSoup
import tkinter as tk
import plyer
import datetime
import time
import requests
from urllib3.util import url

country = input("Enter your country name:")
url = "https://www.worldometers.info/coronavirus/country/{}/".format(country)
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")
print("Total cases:", data[0].text.strip())
print("Total Deaths:", data[1].text.strip())
print("Total Recovered:", data[2].text.strip())


