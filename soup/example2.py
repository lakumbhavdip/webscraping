from bs4 import BeautifulSoup

html = '''<html>
<head>
<title>title of the webpage</title>
<body>
    <p class='odd'>
    this is first paragraph
    </p>
    <p class='even'>
    this is second paragraph
    </p>
    <p class='odd'>
    this is third paragraph
    </p>
     <p class='even'>
    this is fourth paragraph
    </p>
     <p class='odd'>
    this is firth paragraph
    </p>
</body>
</head>
</html>
'''

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
# title = soup.title.get_text()
# print(title)
# body = soup.body.get_text()
# print(body)
# paragraphs = soup.body.find_all('p')
# print(paragraphs)
# for paragraps in paragraphs:
#     print(paragraps.get_text())
    
    
# odds = soup.body.find_all("p",{"class":"odd"})
# # print(odd)
# for odd in odds:
#     print(odd.get_text())
    
# evens = soup.body.find_all("p",{"class":"even"})
# # print(odd)
# for even in evens:
#     print(even.get_text())