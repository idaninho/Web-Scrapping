import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/example.html",
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

print (type(r))
c=r.content
print(c)
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())


#find is only for the first
#find_all for all of them- in place [0] is the first.
all=soup.find_all("div", {"class":"cities"})
#all=soup.find_all("div", {"class":"cities"})[0] ONLY THE FIRST
print(all)
print()
for i in all:#for every DIV find his H2 tag and print only the text
#because we have in this div only one P so we can use find_all or FIND 
    print(i.find_all("h2")[0].text)#for every DIV find his H2 tag and print only the text
    print(i.find("p").text)#because we have in this div only one P so we can use find_all or FIND
    print()
