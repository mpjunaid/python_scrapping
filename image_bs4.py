from bs4 import BeautifulSoup
import requests

from PIL import Image
from io import BytesIO

search =input("Search for:")
params={"q":search}
r= requests.get("https://www.bing.com/images/search",params=params)


soup = BeautifulSoup(r.text,"html.parser")
links=soup.findAll("a",{"class":"thumb"})

for item in links:
    try:
        print("Getting : ",item.attrs["href"])
        img_obj=requests.get(item.attrs["href"])
        title=item.attrs["href"].split("/")[-1]
        img=Image.open(BytesIO(img_obj.content))
        img.save("./images/" + title, img.format)
    except:
        print("image scap failed")