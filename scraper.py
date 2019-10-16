from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# reads data from Seattle's 2013 page
url = "https://www.pro-football-reference.com/teams/sea/2013/gamelog/"
page = urlopen(url).read()

soup = BeautifulSoup(page)
count = 0
table = soup.find("tbody")
pre_df = dict()
features = {'opp', ''}