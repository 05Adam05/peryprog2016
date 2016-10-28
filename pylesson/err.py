try:
    a = 5/0
    print(a)
except ZeroDivisionError as err:
    print('Ты тупой - делишь на ноль')

print('123')

while True:
    try:
        number = int(input("Введите число:"))
        print("Число умноженное на 5: {0}".format(number*5))
        print("10 делим на {0} = {1} ".format(number, 10/number))
        break
    except ValueError:
        print("Дурак - тебе же сказанно введи ЧИСЛО.\
            ЧИСЛО ЧИСЛО Я СКАЗАЛ")
    except ZeroDivisionError:
        print('Ты тупой - делишь на ноль. Введи нормальное число')
    finally:
        print("Ты все равно тупой")


# raise ZeroDivisionError
class TupoyError(Exception): pass

try:
    name = input('Введи имя')
    if name == 'Арсен':
        raise TupoyError
except TupoyError:
    print('Вы ввели Арсен - это очень прекрасно. Фатальная ошибка')