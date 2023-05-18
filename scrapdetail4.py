from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

aplurl = "https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_89%3AApple&dc&ds=v1%3A%2F0X17v%2Bopn%2F%2F2E8eg8gBxlJRKDvjpVc5mpgaLlcAV6g&qid=1684152044&rnid=1389401031&ref=sr_nr_n_2"
file = urlopen(aplurl)
html = file.read()
soup = BeautifulSoup(html,'html.parser')
# print(soup)
iphone = soup.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
# print(dv)
print("----------------------------------------------------------------")
print("---------------------------IPHONE-------------------------------")
print("----------------------------------------------------------------")
a=1
for ip in iphone:
    text = re.sub('<.*?>', '', str(ip))
    print(a,text.strip())
    a+=1


opurl = "https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_89%3AOnePlus&dc&qid=1684152312&rnid=3837712031&ref=sr_nr_p_89_2&ds=v1%3Ag97w6ud24hg1jjpIQL0FCaOmjL9fqv7JxJ4SHEdzX0E"
file = urlopen(opurl)
html = file.read()
soup = BeautifulSoup(html,'html.parser')

oneplus = soup.find_all("span",class_="a-size-base-plus a-color-base a-text-normal")
# print(dv)
print("----------------------------------------------------------------")
print("---------------------------ONEPLUS-------------------------------")
print("----------------------------------------------------------------")
a=1
for op in oneplus:
    text = re.sub('<.*?>', '', str(op))
    print(a,text.strip())
    a+=1