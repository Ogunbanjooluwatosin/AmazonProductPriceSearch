# ---------------------------------imports----------------------------#
import os

import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# ---------------------------------Getting the request from the amazon website----------------------------#
endpoint = "https://www.amazon.com/iPhone-13-Pro-512GB-Gold/dp/B0BGYBBZ9R/ref=sr_1_11?keywords=iphone+13+pro&qid=1683649333&sr=8-11"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
website_response = requests.get(url=endpoint, headers=header)
data = website_response.text
# ---------------------------------Using BeautifulSoup To scrape the Amazon Website----------------------------#
soup = BeautifulSoup(data, "lxml")
amount_of_product = soup.find(name="span", class_="a-offscreen")
price = float(amount_of_product.getText().split("$")[1])


# --------------------------------- Sending an email----------------------------#

if price < 1000:
    email = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]
    smtplib.SMTP("smtp.gmail.com", port=587)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:Hey,from Amazon!\n\nThe price of the iPhone 13 Pro, 512GB, Gold - Unlocked (Renewed Premium) is now ${price}.Here is the link to purchase it now https://www.amazon.com/iPhone-13-Pro-512GB-Gold/dp/B0BGYBBZ9R/ref=sr_1_11?keywords=iphone+13+pro&qid=1683649333&sr=8-11"
                            )
        connection.close()
