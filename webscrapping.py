import requests
import pandas as pd
from bs4 import   BeautifulSoup

response = requests.get("https://www.flipkart.com/search?q=redmi%2010a&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(response.content,"html.parser")

names = soup.find_all('div',class_="KzDlHZ")

name = []
for i in names[0:20]:
          d = i.get_text()
          name.append(d)
print(name) 

prices = soup.find_all('div',class_="Nx9bqj _4b5DiR")
price = []
for i in prices[0:20]:
          a = i.get_text()
          price.append(a)
print(price) 


ratings = soup.find_all('div',class_="XQDdHH")
rating = []
for i in ratings[0:20]:
          b = i.get_text()
          rating.append(b)
print(rating)



images = soup.find_all('img',class_="DByuf4")
image = []
for i in images[0:20]:
          c = i['src']
          image.append(c)
print(image) 



links = soup.find_all('a',class_="CGtC98")
link = []
for i in links[0:20]:
          e = "https://www.flipkart.com"+i['href']
          link.append(e)
print(link) 


df = pd.DataFrame()
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rating
df["Images"]=image
df["Links"]=link

print(df)

df.to_csv("mobiles.csv")