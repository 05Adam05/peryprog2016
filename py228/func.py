def said(word):
    print("Саид, {0}!!!".format(word))

said('красавчиу')
said('тигр')
b = 'торт' 
said(b)

def sum5(a, b):
    c = a * b
    c += 5
    return c

s1 = sum5(3,2)
print(s1)

import math
print(math.sqrt(4))


def shorter(text, n, e = '...'):
    return text[:n-len(e)] + e

print(shorter("Саид и Саблайм", 7))
print(shorter("Саид и Саблайм", 7, e = '**'))
print('Текст', end=' ')
print('Текст2')
for i in range(1,10):
    print('Gadzhi number 1',end=' ')
print()
print(shorter(n = 7, text = "Саид и Саблайм"))

lsd1 = [1, 2]
print(sum5(*lsd1))

def super_sum5(*args):
    s = 0
    for arg in args:
        s += arg
    return s + 5

print(super_sum5(1,1,1,1,1,1))
print(super_sum5(94,1))
print(super_sum5())

ddd1 = {'a':5,'b':6}
print(sum5(**ddd1))

def shopper(**kwargs):
    for key, value in kwargs.items():
        print('Ты купил {0} в колличестве {1} штук'.format(key,value))

shopper(moloko = 6, hleb= 2, rubashki = 12)


def super_sum5_v2(*args,**kwargs):
    """ Это функция -
творит добро
"""
    s = 0
    for arg in args:
        s += arg
    for kwarg in kwargs.values():
        s += kwarg
    return s + 5

print(super_sum5_v2(1,2,a=2,c=3))
print(super_sum5_v2.__doc__)
# print(help(super_sum5_v2))y

def gadzhi(x,y):
    x = y + 7 + x
    global z
    z = 2
    # print(z)
    return x

z = 8
x = 1
y = 2
print(gadzhi(x,y))
print(x)
print(z)


def sp(spisok):
    spisok.append(8)
    print(spisok)


s1 = [2, 4]
# sp(s1)
sp(s1.copy())
print(s1)






