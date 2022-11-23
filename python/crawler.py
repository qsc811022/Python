import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

#建立一個 Requestion物件，附加Request Headers的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
#print(root.title.string)
titles=root.find_all("div",class_="title") #尋找所有clas="Title的"
#print(titles.a.string)
for title in titles:
    if title.a != None:
        print(title.a.string)