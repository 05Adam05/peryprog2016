import random
path = "Garri_Potter_i_Dary_smerti2.txt"
with open(path,"rt", encoding='utf-8') as file:
	text = file.read()
input('Введите ваш вопрос: ')
l = 40
num = random.randint(0,len(text)-l)
ans = text[num:num+l]
print(ans)