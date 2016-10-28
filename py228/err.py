# try:
#     num = 10 / 0
#     print(num)
# except ZeroDivisionError as err:
#     # print(err)
#     print("Ты тупой - делишь на ноль")

print("123")

while True:
    try:
        i = input("Введи число: ")
        i = int(i)
        print("10 делить на {0} = {1}".format(i,10/i))
        break
    except ValueError:
        print("Эй брат. Ты читать умеешь? ВВЕДИ ЧИСЛОООООО")
    except ZeroDivisionError as err:
        print("Ты тупой - делишь на ноль. Введи нормальное число")
    finally:
        print("!!!")

# raise ZeroDivisionError

class TinaError(Exception):
    pass

try:
    name = input("Введите имя: ")
    if name == 'Тина':
        raise TinaError
    print("{0} красавчик".format(name))
except TinaError:
    print("Тина - круче всех. ФАТАЛЬНАЯ ОШИБКА")


