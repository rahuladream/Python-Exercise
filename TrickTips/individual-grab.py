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


def check_price(URL):
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	"""
	m=open('soupw.txt',"wb")
	m.write(soup.prettify().encode("utf-8"))
	m.close
	"""

	print("Working on Link : \n")
	print(URL)

	title = soup.find("h1", {"class": "entry-title"}).get_text().strip()
	author = soup.find("span", {"class": "entry-author"}).get_text().strip()
	content = soup.find("div", {"class": "text-content"})
	date = soup.find("time", {"class": "entry-date"}).get_text().strip()

	with open(r"file_name_save.csv", mode='a') as csv_file:
		header_csv = ['title', 'date', 'author', 'content']
		writer = csv.DictWriter(csv_file, fieldnames=header_csv)
		writer.writerow({'title': title,'date': date ,'author': author, 'content': content})



def push_notification():
	notify = Notify()
	notify.send("Hi the following task is done.. Please check")


if __name__ == '__main__':
	with open(r'filename.csv', mode='rt') as link:
		data = csv.reader(link)
		for row in data:
			check_price(row[4])
	push_notification()