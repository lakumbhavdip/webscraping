
lists=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
from bs4 import BeautifulSoup
from urllib.request import urlopen
zodiac_sign = input("Enter your zodiac sign")
if zodiac_sign in lists:
    WebPageAddress = f"https://www.prokerala.com/astrology/horoscope/?sign={zodiac_sign}"

    file = urlopen(WebPageAddress)
    html = file.read()

    soup = BeautifulSoup(html,'html.parser')

    print(soup.body.find("article").get_text())

   
else :
   print (f"invalid zodic_sign := {zodiac_sign}")