from collections import Counter

phones = ["Iphone", "Savsung", "LG","Iphone" , "LG"]

count = Counter(phones)

print(count)


text = "Ехал Грека через реку видит Грека в реке рак"
count = Counter(text.lower().replace(" ", ""))
print(count)