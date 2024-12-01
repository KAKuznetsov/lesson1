from pprint import pprint

product = {
    "name": "Xiaomi 14 Ultra",
    "stock": 24,
    "price": 93344

}

recomendation = ['Раз рекомендация', "два рекомендация", "Три супер пупер рекомендатион супер пупер аут пупер"]
print(product)
product["memory"] = 512
print(len(product))
print(product.keys())
print(product.values())
print(product.items())
print(product.get("discount", "А вот никто не знает скидку"))
product['recomendation'] = recomendation
pprint(product)
product['recomendation'].append("А вот и четвертая рекомендашка, да")
pprint(product)

for i in product.keys():
    print(i)

x = list(product.keys())   
print (type(x)) 
pprint(x)