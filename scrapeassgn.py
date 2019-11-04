import requests, mechanize
from bs4 import BeautifulSoup
import csv

csvfile = open('scrapeassgn.csv','w', newline='')
hwy_write = csv.writer(csvfile)

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table',{'class':'accidentOutput'})

rows = main_table.find_all('tr')

for r in rows:
	cells = r.find_all('td')
	data = []

	if len(cells) > 0:
		for c in cells:
			data.append(c.text.strip())

		hwy_write.writerow(data)

csvfile.close()





#it runs and works in command line