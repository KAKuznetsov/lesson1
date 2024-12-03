balance = 100
price = 50
in_stock = 0

print(bool(balance>price))

print(bool(in_stock))

if balance > price and in_stock:
    print("Одобрямс! Можно оплачивать.")
elif not in_stock:
    print("К сожалению товара нет в наличии")
else:
    print("Отобой! Сначала пополните баланс.")



def check_weather(temperature):
    if temperature <0:
        return  "На улице холодно"
    elif temperature >= 0 and temperature < 15:
        return  "На улице прохладно"
    elif temperature >= 15 and temperature < 25:
        return  "На улице тепло"
    else:
        return "На улице жарко"

print (check_weather(-10)) # "На улице холодно"
print (check_weather(8)) # "На улице прохладно"
print (check_weather(20)) # "На улице тепло"
print (check_weather(30)) # "На улице жарко"

