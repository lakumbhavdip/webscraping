#find a user are enter a city and is city's temprature 

from bs4 import BeautifulSoup
from urllib.request import urlopen
city=input("enter a city name = ")
WebPageAddress = f"https://www.weather-forecast.com/locations/bhavnagar/forecasts/latest"
file = urlopen(WebPageAddress)
html = file.read()
soup = BeautifulSoup(html,'html.parser')
weather =soup.body.find("tr",{"class":"b-forecast__table-description b-forecast__hide-for-small days-summaries js-day-summary"})
for temprature in weather:
    print(temprature.get_text())