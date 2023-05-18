from bs4 import BeautifulSoup
from urllib.request import urlopen
zodiac_sign = input("Enter your zodiac sign")
WebPageAddress = f"https://www.prokerala.com/astrology/horoscope/?sign={zodiac_sign}"
file = urlopen(WebPageAddress)
html = file.read()
soup = BeautifulSoup(html,'html.parser')

print(soup.body.find("article").get_text())