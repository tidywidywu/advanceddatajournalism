import urllib2, csv #says to import code from libraries
from bs4 import BeautifulSoup #same as above

outfile = open('jaildata.csv', 'w') #opens or creates a pathway to a file of that name 
writer = csv.writer(outfile) #allows us to write to that file

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500' #define the URL we're scraping
html = urllib2.urlopen(url).read() #open the URL we're looking at and reads it

soup = BeautifulSoup(html, "html.parser") #using BeautifulSoup, examine and parse the html

tbody = soup.find('tbody', {'class': 'stripe'}) #from the parsing, find position of 'tbody' within dictionary between class and stripe

rows = tbody.find_all('tr') #find all 'tr' within tbody

for row in rows: #for all the row within rows

    cells = row.find_all('td') #define cell as all 'td' 

    data = [] #create data first as a empty list
    for cell in cells: #for all specific td in 'tds'
        data.append(cell.text.encode('utf-8')) #add to list certain code that will scrape

    writer.writerow(data) #write that result into the csv file