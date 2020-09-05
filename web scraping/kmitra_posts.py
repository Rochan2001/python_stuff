import requests
from bs4 import BeautifulSoup
source = requests.get("https://kmit.in/emagazine/")
soup = BeautifulSoup(source.content, "html.parser")
containers = soup.find_all("div","post-container")
container = containers[0]
titles = soup.find_all("h2","post-title")
authors = container.find_all("a", "author url fn")
post = container.find("div",'post-excerpt').p
post_=list(post)
posts = [x for x in post if x is not container.find("a", "more-link")]
for container in containers:
    title = container.find_all("h2","post-title")
    authors = container.find_all("a","author url fn")
    post = list(container.find("div", 'post-excerpt').p)
    posts = [x for x in post if x is not container.find("a", "more-link")]
    print("Title : "+title[0].text)
    print("Authors : ")
    for i in range(len(authors)):
        print(authors[i].text)
    print("Post excerpt : "+ posts[0])    
    print("")

