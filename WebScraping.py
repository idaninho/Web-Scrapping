import requests
import pandas
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

l=[]
for item in all:#instead of the print method, we define a dictionary and define all of its keys.
    d={}
    d["Price"]=item.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")
    d["Address"]=item.find_all("span", {"class":"propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span", {"class":"propAddressCollapse"})[1].text
    try:
        d["Beds"]=item.find("span", {"class":"infoBed"}).find("b").text#only the numbers, without the word BED
    except:
        d["Beds"]="No Info On Beds"

    try:
        d["Full Baths"]=item.find("span", {"class":"infoValueFullBath"}).find("b").text#only the numbers, without the word FULL BATH
    except:
        d["Full Baths"]="No Info On Baths"

    try:
        d["Half Baths"]=item.find("span", {"class":"infoValueHalfBath"}).find("b").text#only the numbers, without the word HALF BATH
    except:
        d["Half Baths"]="No Info On Half Baths"

    try:
        d["Area"]=item.find("span", {"class":"infoSqFt"}).find("b").text#only the numbers, without the word SQFT
    except:
        d["Area"]="No Info On SQFT"

    for column in item.find_all("div", {"class":"columnGroup"}):
        #print(column)
        for feature_group, feature_name in zip(column.find_all("span", {"class":"featureGroup"}), column.find_all("span", {"class":"featureName"})):
            #print (feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    l.append(d)
#print(l)
#print(len(l))

df=pandas.DataFrame(l)
df.to_csv("Output.csv")
