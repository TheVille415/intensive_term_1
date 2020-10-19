import requests
from bs4 import BeautifulSoup as bs
#website listing
r = requests.get("https://www.ebay.com/itm/Kirkland-Signature-High-Performance-3-Piece-Wedge-Set-52-56-60/154144483938?hash=item23e3ba2a62:g:DYsAAOSwvvhfiLCH")
#content of the website in HTML
soup = bs(r.content)

#selects line of html 
price = soup.select(".notranslate")
print(price)

#another way to find the link of html
divs = soup.select('span#prcIsum')
print(divs[0])

#saving the webpage to a text file
file1 = open("scrapper.txt", "w")
file1.write(soup.prettify())