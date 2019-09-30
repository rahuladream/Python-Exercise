"""
Price alert for amzon and sending and push notification
"""

import requests, time, smtplib,math
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime
from price_parser import Price

'''
url = input('Enter your URL here : ')
dp = int(input('Enter your desired price : '))
'''

url = "https://www.amazon.in/Mi-20000mAH-Li-Polymer-Sandstone-Charging/dp/B07VXJS7DH/ref=lp_18452597031_1_5?s=electronics&ie=UTF8&qid=1569709854&sr=1-5"
desired_price = 1199.00
URL = url
pnmsg = "Below Rs. "+str(desired_price)+" You can get"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	"""
	m=open('soupw.txt',"wb")
	m.write(soup.prettify().encode("utf-8"))
	m.close
	"""
	title = soup.find(id="productTitle").get_text().strip()
	price = soup.find(id="priceblock_dealprice").get_text()
	main_price = Price.fromstring(price[2:])

	print("NAME : "+ title)
	print("CURRENT PRICE : "+ str(main_price.amount_text))
	print("DESIRED PRICE : "+ str(desired_price))

	count = 0
	if(main_price.amount_float <= desired_price):
		send_mail()
		push_notification()
		print("Email and notification sent")
		exit(0)
	else:
		count += 1
		print("Rechecking the price... Last check price at {}".format(datetime.now()))

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('xyz@gmail.com', 'zxyz@123')
	subject ="Mi 20000mAH Li-Polymer Power Bank 2i  price has fallen below Rs. "+ str(desired_price)
	body =  "Hey Prabhu! \n The price of Iphone XR 64GB on AMAZON has fallen down below Rs."+str(desired_price)+".\n So, hurry up & check the amazon link right now : "+url

	msg = f"Subject: {subject} \n\n {body} "
	server.sendmail(
		'myemailtobenotified@gmail.com',
		msg)

def push_notification():
	notify = Notify()
	notify.send(pnmsg)


if __name__ == '__main__':
	count = 0
	while (True):	
		count += 1
		print("Count {}".format(str(count)))
		check_price()
		time.sleep(5)