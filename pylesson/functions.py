def hello(name):
    print('Дратути, {0}!!!'.format(name))

m = 'Гаджи'
hello('Иса')
hello('Руслан')
hello(m)

def sum5(a, b):
    s = a + b + 5
    return s

num1 = sum5(4,5)
print(num1)
num2 = sum5(4,num1)
print(num2)

if sum5(1,5) > 10: print('>10')

print(sum5(5,2))
print(sum5(b = 5, a = 2))

def less_text(text,n,end='...'):
    return text[:n-len(end)] + end

print(less_text('Ла ла ла ',7))
print(less_text('Ла ла ла ',8,end='***'))


print('Привет', end=' ')
print('Привет')

my_args = (1, 6)

print(sum5(*my_args))

def mul(*args):
    m = 1
    for arg in args:
        m *= arg
    return m

print(mul(3,3,3))

print(mul(1,1,1,1,1,1,94))

def cloth(head,body,legs='штаны рыбака'):
    return {'голова':head,'тело':body,'ноги':legs}



malchic1 = cloth('кепка','майка','трусы')
print(malchic1)

ruslan = cloth(body='шлем золотой',head='золотой нагрудник')
print(ruslan)

cl = {'head':'шлем золотой','body':'золотой нагрудник','legs':'трусы'}
ruslan = cloth(**cl)
print(ruslan)

def shop(**kwargs):
    """ Эта крутая функция выводит все
именнованные покупки
"""
    for key, item in kwargs.items():
        print('Покупаем {0}: {1} штук'.format(key,item), end= ". ")
    print()



shop(moloko = 5, sir = 6, hleb = 2, snikers = 10) 
print(shop.__doc__)

def super(a, b):
    # a = b - a
    global c 
    c = 15
    print(c)
    b.append(16)


c = 5
a = 3
b = [10,20]
super(a,b)
# super(a,b.copy())
# print(a)
# print(b)
print(c)
print(b)