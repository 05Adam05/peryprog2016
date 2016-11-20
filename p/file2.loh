f1 = open('kak-vsegda.txt','wt',encoding='utf-8')
f1.write('Что либо.\n')
f1.write('Тагир любит кофе с молоком.\n')
print('Исак вернулся!', file=f1)
f1.close()

f2 = open('kak-vsegda.txt','rt',encoding='utf-8')
text = f2.read()
f2.close() 
print(text)

f2 = open('kak-vsegda.txt','rt',encoding='utf-8')
text = f2.readline()
f2.close()
print(text)

f2 = open('kak-vsegda.txt','rt',encoding='utf-8')
for line in f2:
	if not 'кофе с молоком' in line:
		print(line)
f2.close()

stih = """Сагитав хороший парень
дальше мат"""

with open('saga.txt','wt',encoding='utf-8') as f:
	f.write(stih)


