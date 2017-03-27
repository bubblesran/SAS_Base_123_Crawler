#-*- coding:utf-8 -*- #

import urllib
from bs4 import BeautifulSoup
import sys

indexurl = 'http://sas.1or9.com/archives/sas-certified-base-programmer-123-questions-%d'

def get_content(url):
	page = urllib.request.urlopen(url)
	contents = page.read()
	soup = BeautifulSoup(contents)
	result = soup.find("div", {"class":"padding10"}).text
	return result

def main():
	global indexurl
	words = []
	for i in range(1,124):
		url = indexurl % i
		text = get_content(url)
		words.append(text)
	total = '\r'.join(words)
	with open('sasbase_123.txt', 'w', encoding="utf-8") as text_file:
		text_file.write(total)

if __name__ == '__main__':
	main()

