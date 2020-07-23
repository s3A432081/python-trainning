import requests as req
from bs4 import BeautifulSoup
import shutil
res = req.get("https://promotion.asialife-go.com/2-0-promo/")
soup = BeautifulSoup(res.text,"html.parser")

titles = soup.find_all("h4",class_="elementor-heading-title elementor-size-default")
imgs = soup.find_all("div",class_="elementor-image")
results = soup.find_all("div",class_="elementor-button-wrapper")

i=0
while i <= len(results):
    print("商店名稱：",titles[i+1].text)
    print("商店照片：",imgs[i+1].find("img").get("src"))
    print("上架狀態：",results[i].find("span",class_="elementor-button-text").text)
    print("商店網址：",results[i].find("a").get("href")+"\n")
    i +=1
