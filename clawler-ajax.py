import urllib.request as req
url="https://medium.com/_/graphql"

    #建立一個 Requestion物件，附加Request Headers的資訊
request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    })

with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #print(data)

#解析 json格式的資料
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data)
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])