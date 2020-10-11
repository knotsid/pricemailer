import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
url = "https://www.flipkart.com/logitech-mk275-mouse-wireless-laptop-keyboard/p/itmerzve2q3cauzn?pid=CASERZVE4RFEG5JZ&cmpid=product.share.pp"

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

def check_price():

    page = requests.get(url, headers = header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs="_35KyD6").get_text()
    price = soup.find(attrs="_1vC4OE _3qQ9m1").get_text()
    conv_price = price[1:6]
    conv_price = conv_price.replace(",", "")
    new_price = int(conv_price)
    old_price = new_price
    if new_price < old_price:
        send_mail()
        old_price = new_price

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("msammy237@gmail.com", "wtvccdjdekhvdodb")

    subject = "Keyboard price is reduced"
    body = "Check the link \n https://www.flipkart.com/logitech-mk275-mouse-wireless-laptop-keyboard/p/itmerzve2q3cauzn?pid=CASERZVE4RFEG5JZ&cmpid=product.share.pp"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'msammy237@gmail.com',
        'kumarsid6500@gmail.com',
        msg
    )
    print("Email has sent!!!!!!!")

    server.quit()

while True:
    check_price()
    sleep(3 * 60 * 60)