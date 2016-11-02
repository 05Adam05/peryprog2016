def add7(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return res + 7
    return wrapper

def tupit(a):
    return a

@add7
def sum5(a):
    return a + 5

@add7
def mul2(a,b):
    return (a + b) * 2

print(tupit(sum5)(4))

# num = add7(sum5)
# print(num(2))
print(sum5(3))
print(mul2(1,3))

def sort_last(e):
    return e[-1]

s = lambda a: a + 7
print(s(1))
print(lambda: 'привет')
god_boys = ['саид', 'али', 'Абурахман','Гаджир']
god_boys.sort(key = lambda e: e.lower())
god_boys.sort(key = lambda e: e[-1])
god_boys.sort(key = sort_last)
print(god_boys)

useless = lambda f: lambda *args, **kwargs: f(*args, **kwargs) + 1

@useless
def sum4(a):
    return a + 4

print(sum4(1))