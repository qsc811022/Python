# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")

# print(data)


import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/08a7c7ba-f07c-442a-8310-0a9ab9f49905?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)

clist=data["result"]["results"]
for company in clist:
    print(company["program"])