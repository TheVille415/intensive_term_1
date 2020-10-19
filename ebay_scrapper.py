import requests
from bs4 import BeautifulSoup as bs
#website listing
r = requests.get("https://www.ebay.com/itm/Kirkland-Signature-High-Performance-3-Piece-Wedge-Set-52-56-60/154144483938?hash=item23e3ba2a62:g:DYsAAOSwvvhfiLCH")
#content of the website in HTML
soup = bs(r.content)

#another way to find the link of html
price_line = soup.select('span#prcIsum.notranslate')
print(price_line[0])

#saving the webpage to a text file
file1 = open("/Users/Jordan/dev/Make School Courses/Intensive/Term 1/scrapper.txt", "w")
file1.write(soup.prettify())
#saving the line of html to the end of the file
file1.write(str(price_line))
file1.close()