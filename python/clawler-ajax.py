import urllib.request as req
import json
url="https://medium.com/_/graphql"

#requestData
requestData=[{"operationName":"CollectionViewerEdge","variables":{"collectionId":"544c7006046e"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"},{"operationName":"CollectionViewerEdge","variables":{"collectionId":"15f753907972"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"},{"operationName":"CollectionViewerEdge","variables":{"collectionId":"cb2fe8af86cb"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"},{"operationName":"CollectionViewerEdge","variables":{"collectionId":"138adf9c44c"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"}]


    #建立一個 Requestion物件，附加Request Headers的資訊
request=req.Request(url, headers={
        "content-type":"application/json",
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
},data=json.dumps(requestData).encode("utf-8"))

with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

result=json.loads(data)
#items=result["id"]
print(result)
# for item in items:
#     print(items["data"]["collectionId"])
#print(data)

#解析 json格式的資料
# import json
# data=data.replace("])}while(1);</x>","")
# data=json.loads(data)
# posts=data["payload"]["references"]["Post"]
# for key in posts:
#     post=posts[key]
#     print(post["title"])



