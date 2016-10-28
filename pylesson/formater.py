name = 'Исак'
num = 1000000
print("%s крутой программист" % name)

print("У %sа %d рублей" % (name, num))
num2 = 20.5
print("%s делится на %f %d" % (name, num2, 50))
print("%5.3s делится на %5.3f %5.3d" % (name, num2, 50))

print("{} делится на {} и {}".format(name, num2, 50))

print("{1} делится на {2} и {0}".format(name, num2, 50))

print("{2} делится на {1} и {0}".format(name, num2, 50))

print("{m1} {m2} {m3}".format(m1="Арсен", m2="любит", m3="Руслана"))


isa = {'name':'Иса','surname':'Чупаниспев','age':11}

print("Имя: {0[name]}, фамилия: {0[surname]}, \
    возраст: {0[age]} - {1}".format(isa, "красавчик"))

print("{2} делится на {1} и {0:-^20.3s}".format(name, num2, 50))