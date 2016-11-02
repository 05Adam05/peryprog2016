def mul5(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs) * 5
    return wrapper


def py228(a):
    return a

@mul5
def sum5(a):
    return a + 5

@mul5
def sum7(a,b):
    return a + b + 7

# print(sum5(4))

# print(py228(sum5)(6))

# m = mul5(sum5)

# print(m(4))

print(sum5(3))
print(sum7(2,4))

def dota2():
    return 'Дота фигня'

print(dota2())

dota = lambda: 'Дота фигня'

print(dota())

lst1 = ['Сагид','Амир','Пудж','паренек толстенький','артур']

def sort_last(e):
    return e[-1]

lst1.sort(key= lambda e: e.lower())
lst1.sort(key= lambda e: e[-1])
lst1.sort(key= sort_last)
print(lst1)