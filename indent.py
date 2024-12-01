import random

x = random.randint(0,10)

def more_or_less(num):
    if x >= 5:
        print ("Больше!")
    else:
        print("Неа, меньше!")

more_or_less(x)        


y = 0

while y < 10:
    print(y)
    y = y +1 