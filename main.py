from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

url = "https://www.amazon.in/Noise-Bluetooth-Wireless-30-Hours-Instacharge/dp/B09Y5MP7C4/ref=sr_1_1_sspa?crid" \
      "=K09C2PICJ8V2&keywords=tws&qid=1669488079&qu=eyJxc2MiOiI3LjQ1IiwicXNhIjoiNy4yNSIsInFzcCI6IjYuMTQifQ%3D%3D" \
      "&sprefix=tw%2Caps%2C294&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1 "

headers = {
    'Accept-Language': "en-US,en;q=0.6",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36 "
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen")
price_li = price.text.strip("₹ .00").split(",")
final_price = int(price_li[0] + price_li[1])

my_email = SENDERS_EMAIL
recievers_email = RECIEVERS_EMAIL
my_pass = SENDERS_PASSWORD

if final_price < 1000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recievers_email,
            msg=f"Python price drop alert!\n\n Final price is {final_price}.\nCheck it! "
        )
