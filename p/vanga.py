from random import randint

path = 'Garri_Potter_i_Dary_smerti2.txt'
f1 = open(path,'rt',encoding = 'utf-8')
text = f1.read()
f1.close()

l = 40
start = randint(0,len(text)-l)
answer = text[start:start+l]

q = input("Введите ваш вопрос: ")
print(answer)