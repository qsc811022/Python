# #儲存檔案
# file = open("data.txt", mode="w", encoding="utf-8")
# #讀取檔案
# file.write("Hello File\nSecond Line\n測試")
# file.close()
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello File\nSecond Line\n測試111")

#讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
        data=file.read()
print(data)

#使用Json 格式讀取