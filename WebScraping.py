import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/",
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})


#print (type(r))
c=r.content
#print(c)
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all= soup.find_all("div", {"class":"propertyRow"})
print(all[0].find_all("h4",{"class":"propPrice"})[0].text.replace("\n","").replace(" ",""))#FIND also is good
print(len(all))

for item in all:
    print(item.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span", {"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span", {"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span", {"class":"infoBed"}).find("b").text)#only the numbers, without the word BED
    except:
        print("No Info On Beds")

    try:
        print(item.find("span", {"class":"infoValueFullBath"}).find("b").text)#only the numbers, without the word FULL BATH
    except:
        print("No Info On Baths")

    try:
        print(item.find("span", {"class":"infoValueHalfBath"}).find("b").text)#only the numbers, without the word HALF BATH
    except:
        print("No Info On Half Baths")

    try:
        print(item.find("span", {"class":"infoSqFt"}).find("b").text)#only the numbers, without the word SQFT
    except:
        print("No Info On SQFT")
    print()
