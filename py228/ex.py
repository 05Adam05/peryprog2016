# try:
#     x = 5 / 0
#     print(x)
# except ZeroDivisionError as err:
#     # print(err)

print(123)

while True:
    try:
        num = int(input("Введите число: "))
        print("Десять деленное на {0} = {1}".format(num,10/num))
        break
    except ValueError:
        print('Ты дурак. ТЫ вообще умеешь читать.\
Да? Там что написанно? ВВЕДИ ЧИСЛО')
    except ZeroDivisionError as err:
        print("Ты тупой - делишь на ноль. Введи НОРМАЛЬНОЕ число")
    finally:
        print('=)')


# raise ZeroDivisionError

class TagirError(Exception): 
    pass

try:
    name = input("Введите имя: ")
    if name == 'Тагир':
        raise TagirError
    print("{} красавчик".format(name))
except TagirError:
    print("Тагир - ультракрасавчик. ФАТАЛЬНАЯ ОШИБКА")

