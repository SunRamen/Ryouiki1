import json

with open('catalog.json','r',encoding='UTF-8') as f:
        dict = json.load(f)
c = 0
max = 0
min = 1000000000
for i in dict:
        if i["name"] == "jacket":
                c += 1
                if i["price"] > max:
                        max = i["price"]
                if i["price"] < min:
                        min = i["price"]

print("jacketの個数 =",c)
print("最高価格 = ",max)
print("最低価格 = ",min)
