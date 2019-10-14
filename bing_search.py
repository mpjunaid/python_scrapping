from bs4 import BeautifulSoup
import requests

message=input("Enter to search : ")
params ={"q":message}
r= requests.get("https://www.bing.com/search",params=params)

soup=BeautifulSoup(r.text,"html.parser")
#print(soup.prettify())  to print the html

results=soup.find("ol",{"id":"b_results"})
links=results.findAll("li",{"class":"b_algo"})


for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text,':',item_href)
