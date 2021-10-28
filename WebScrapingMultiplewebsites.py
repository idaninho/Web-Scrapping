import requests
import pandas
from bs4 import BeautifulSoup



l=[]

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c=r.content
soup=BeautifulSoup(c,"html.parser")
soup.prettify()
pageNum=soup.find_all("a", {"class":"Page"})[-1].text

base_url="https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(pageNum*10),10):
    print(base_url+str(page)+".html")
    r = requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    soup.prettify()
    all= soup.find_all("div", {"class":"propertyRow"})

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
            for feature_group, feature_name in zip(column.find_all("span", {"class":"featureGroup"}), column.find_all("span", {"class":"featureName"})):
                #print (feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text
        l.append(d)

df=pandas.DataFrame(l)

df.to_csv("OutputMultiPages.csv")
