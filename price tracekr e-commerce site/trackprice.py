import requests
from bs4 import BeautifulSoup
import time
import webbrowser


def find_price(URL):
    req = requests.get(URL, headers={
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"})
    soup = BeautifulSoup(req.text, "html.parser")

    try:
        if 'amazon' in URL:
            price = soup.find('span', class_="a-offscreen")

            return price

        elif 'flipkart' in URL:
            price = soup.find(class_="_30jeq3 _16Jk6d")
            return price
        elif 'ajio' in URL:
            price = soup.find(class_="prod-sp")
            return price

    except:
        return

i=1
URL = input("Enter the link: ")
while True:
    price = find_price(URL)
    if price == None:
       price("This link is invalid ,please take the valid Link.")
       break
    else:
        if(i<2):
            curr_price=price.text
        prev_price = curr_price
        print(f"Current price this product - {price.text}")
        
        if(i>2):
            curr_price =price.text
            if(curr_price !=prev_price):
                webbrowser.open_new(URL)
        time.sleep(60)


# URL="https://www.amazon.in/dp/B09WVZ2ZSS?ref_=cm_sw_r_apan_dp_3B8X75Z29YP02YV4GHQS"
# req =requests.get(URL ,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"})
# soup = BeautifulSoup(req.text,"html.parser")
# price = soup.find(class_="a-offscreen")
# print(price.text)
