import pizzeria

summa = 0
while True:
    zakaz = input("Введите заказ: ")
    if zakaz in pizzeria.pizzas:
        summa = pizzeria.zakazat(zakaz, summa)
        print(summa)
    else:
        print("Нет такой пиццы")
    if summa > 1000:
        print("Вы уже обожрались. Хватит хавать.")
        break