def my_func(a):
    return a

def mul5(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs) * 5
    return wrapper

@mul5
def sum5(a):
    return a + 5

@mul5
def mmm(a,b):
    return a * b * 3


# print(my_func(sum5)(5))



# m = mul5(sum5)

# print(m(5))

print(sum5(3))

print(mmm(1,2))

sum52 = lambda a: a + 52

print(sum52(50))

list1 = ['Руслан','артур', 'Абдул', 'рашид']

# list1.sort(key = lambda e: e.lower())
# list1.sort(key = lambda e: e[1])
def second(e):
    return e[1]

    
list1.sort(key = second)
print(list1)