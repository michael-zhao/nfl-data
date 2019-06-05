from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/teams/sea/2019.htm"
page = urlopen(url).read()
print(page)

# soup = BeautifulSoup(page)
  # count = 0
  # table = soup.find()