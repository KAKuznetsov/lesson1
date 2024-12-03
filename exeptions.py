def cut_cake(peaple):
    try:
        parts = 1 / peaple
        print(f'Каждый человек получит {parts} пирога')
    # except ArithmeticError:
    #     print("Пожалуйста, не делите на ноль!")
    # except TypeError:
    #     print("Пожалуйста, вводите число, а не какие-то там строки!")
    except(ArithmeticError,TypeError ):
        print("Ну сорри, не могу ничего сделать блин и взять и поделить!")

    except KeyboardInterrupt:
        print("Остановлено пользователем через клавиатуру с помощью контрл С!")

cut_cake(5)
cut_cake(0)
cut_cake('5')

# import random 

# while True:
#     p = random.randint(1,10)
#     cut_cake(p)

