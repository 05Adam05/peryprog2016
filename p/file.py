# f1 = open('arsen.txt','wt', encoding = 'utf-8')
# f1.write('Арсен любит мороженное\n')
# arsen_hate = '\tОфициальный сайт Хайванов'
# f1.write(arsen_hate)
# f1.close()

f2 = open('arsen.txt','rt', encoding = 'utf-8')
text = f2.read()
f2.close()
print(text)

f2 = open('arsen.txt','rt', encoding = 'utf-8')
lst_text = []
for line in f2:
	lst_text.append(line)
	print(line)
f2.close()
print(lst_text)


f2 = open('arsen.txt','rt', encoding = 'utf-8')
text = f2.read(10)
f2.close()
print(text)

isa_text = """Иса такой хороший мальчик
Он любит котят четкие
ла ла ала"""

with open('isa','wt', encoding = 'utf-8') as f3:
	f3.write(isa_text)