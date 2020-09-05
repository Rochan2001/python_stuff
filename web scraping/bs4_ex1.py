import requests
from bs4 import BeautifulSoup
source = requests.get(
    "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards")
page_soup = BeautifulSoup(source.content, "html.parser")
containers = page_soup.find_all('div', class_="item-container")
out_filename = "graphics_cards.csv"
headers = "brand,product_name,shipping \n"
f = open(out_filename, "w")
f.write(headers)

contain = containers[0]
container = containers[0]
 #print(container.find("div", "item-info").a.img['title'])
x = container.find("div", "item-info").a.img.get("title")
for container in containers:
    brand = container.find("div", "item-info").a.img.get("title")
    title_container = container.find_all('a', class_="item-title")
    product_name = title_container[0].text
    shipping_container = container.find_all("li","price-ship")
    shipping = shipping_container[0].text.strip()
    print("brand : " + brand)
    print("product_name : " + product_name)
    print("shipping : " + shipping)
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")
f.close()
