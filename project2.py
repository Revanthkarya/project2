
import requests
from bs4 import Beautifulsoup
import pandas
import argparse

parser = argparse.Argumentparaser()
parser.add_argument("--page_num_MAX", help="enter the  number of pages to parse", type=int)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-chennai/?page="
page_num_MAX = args.page_num_MAX
scraped_info_list = []

for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url + str(page_num))
    content = req.content

    soup = Beautifulsoup(content,"html.parser")

    all_hotels = soup.find_all("div",{"class": "hotelcardlisting"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHoteldescription_hotelname"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class": "listingprice_finalprice"}).text
        try:
         hotel_dict["rating"] = hotel.find("span", {"class": "hotelrating_ratingsummary"}).text
