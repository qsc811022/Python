from flask import Flask
app=Flask(__name__) #_name_現在的模組

@app.route("/") #函式的裝飾(Decorator):以函式為基礎 提供附加的功能
def home():
    return "hello Flask"

@app.route("/test")
def test():
    return "This is Test"



if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動