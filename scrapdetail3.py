
from urllib.request import Request,urlopen
import re
from bs4 import BeautifulSoup 

url = "https://wanbuffer.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

req = Request(url, headers=headers)
file = urlopen(req)
html = file.read()
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify)
industryname = soup.find_all("h5",class_="pb-3")
# print(industryname)
print("--------------------------------------------------------------Industry Name--------------------------------------------------------------")
c=1
for element in industryname:
    text = re.sub('<.*?>', '', str(element))
    print(c,text.strip())
    c+=1
    
print("--------------------------------------------------------------Company branch and address--------------------------------------------------------------")

address = soup.find_all("div",class_="footer_inr_address col-6 pb-4")
# print(add)
a= 1
for add in address:
    text = re.sub('<.*?>', '', str(add))
    print(a,text.strip())
    a+=1
    print("-----")
    
    
    