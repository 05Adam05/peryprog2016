def hello(name):
    print('Привет, {0}!!!'.format(name))

n = 'Тина'
hello('Азамат')
print(hello('Баракят'))
hello(n)

def sum5(a, b):
    s = a + b
    s = s * 5
    return s

res = sum5(4,2)
print(res)
print(sum5(2,2))

import math
print(math.sqrt(4))

def shorter(text, n, e = '...'):
    return text[:n-len(e)] + e

print(shorter("Привет пока до с ви да ни я",12))
print(shorter("Привет пока до с ви да ни я",12,'**'))

for i in range(1,10):   
    print('Тина', end = ' ')
print('Молодец')

print(shorter(n = 12, text = "Привет пока до с ви да ни я"))

t1 = (4, 2)

print(sum5(*t1))

def sum_all5(*args):
    s = 0
    for arg in args:
        s += arg
    return s + 5

print(sum_all5(1,1,1,1,1,1))
print(sum_all5(10,20))
print(sum_all5())

dct1 = {'a': 3, 'b': 5}
print(sum5(**dct1))

def shopping(**kwargs):
    for key, value in kwargs.items():
        print('Вы купили {0} за {1} рублей'.format(key,value))


shopping(moloko = 100, miaso = 210, morkovka = 60, prosto = 30 )


def coo(x,y):
    x = x + y*2
    print(z)
    global z
    z = 94
    return x

z = 5
x = 1
y = 2
print(coo(x,y))
print(x)
print(z)

def sp(a):
    a.append(88)

m = [2,3]
# sp(m)
sp(m.copy())
print(m)


