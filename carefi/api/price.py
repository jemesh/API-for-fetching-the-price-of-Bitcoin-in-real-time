import json

from bs4 import BeautifulSoup as BS
import requests
# method to get the price of bit coin
def get_price():
    # getting the request from url
    url = "https://www.google.com/search?q=bitcoin+price"
    data = requests.get(url)
    # converting the text
    soup = BS(data.text, 'html.parser')
    # finding metha info for the current price
    ans = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    # returning the price
    return ans
y=get_price()
m=dict()
m['price']=y
print(m)
