"""
Grab the specific post and store somewhere into the db or file
"""

import requests, time, smtplib,math
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime
from price_parser import Price
import re
import csv
'''
url = input('Enter your URL here : ')
dp = int(input('Enter your desired price : '))
'''

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
URL = "https://www.pyimagesearch.com/category/deep-learning-2/"

def check_price(URL,i):
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	"""
	m=open('soupw.txt',"wb")
	m.write(soup.prettify().encode("utf-8"))
	m.close
	"""

	# findPost = soup.findAll("div", {"class": "up-up-child col-sm-6"})

	# with open(r"file_name_to_save.csv", mode='a') as csv_file:
	# 	header_csv = ['title', 'date', 'summary', 'category', 'link']
	# 	writer = csv.DictWriter(csv_file, fieldnames=header_csv)
	# 	for post in findPost:
	# 		date = post.find("time", {"class": "entry-date"}).get_text().strip()
	# 		title = post.find("h3", {"class": "entry-title"}).get_text().strip()
	# 		summary = post.find("div", {"class": "i-summary"}).get_text().strip()
	# 		category = post.find("span", {"class": "i-category"}).get_text().strip()
	# 		link = post.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
	# 		print({'title': title, 'date': date, 'summary': summary, 'category': category, 'link': link})
	# 		writer.writerow({'title': title, 'date': date, 'summary': summary, 'category': category, 'link': link})
	# title = soup.find(id="productTitle").get_text().strip()
	# price = soup.find(id="priceblock_dealprice").get_text()
	# main_price = Price.fromstring(price[2:])

	# print("NAME : "+ title)
	# print("CURRENT PRICE : "+ str(main_price.amount_text))
	# print("DESIRED PRICE : "+ str(desired_price))

	# count = 0
	# if(main_price.amount_float <= desired_price):
	# 	send_mail()
	# 	push_notification()
	# 	print("Email and notification sent")
	# 	exit(0)
	# else:
	# 	count += 1
	# 	print("Rechecking the price... Last check price at {}".format(datetime.now()))


def push_notification():
	notify = Notify()
	notify.send(pnmsg)


if __name__ == '__main__':
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	findLink = soup.find_all('a')
	for post in findLink:
		print(post)
		print( " ----------------------- ")
		# postLink = post.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
		# print(postLink)