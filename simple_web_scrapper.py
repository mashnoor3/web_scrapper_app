'''
Goal:
To learn webscraping using BeautifulSoup.
Simple script to scrape playstation store home page for newest games to
export title and price of game to csv file.
'''

# Import dependencies
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv

# Read input url
my_url = "https://store.playstation.com/en-ca/home/games"

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# Create BeautifulSoup object and parse for required info
page_soup = bs(page_html, "html.parser")

titles = page_soup.find_all("div",{"class":"grid-cell__title"})
prices = page_soup.find_all("h3",{"class":"price-display__price"})

# Write to csv file
filename = "games.csv"
f = open(filename, "w")

headers = "Game Title, Price ($)"
f.write(headers + "\n")

for i in range(len(titles)):
    game_name = titles[i].string
    game_price = prices[i].string
    print ("Title: {} Price: ${}".format(game_name, game_price))

    f.write(game_name.replace(",", " ") + "," + game_price + "\n")

f.close()
