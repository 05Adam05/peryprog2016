file1 = open('gadji.txt','at', encoding = 'utf-8')
file1.write('Гаджи про или лох вот в чем вопрос?\n')
file1.write('\tКонечно он ***\n')
file1.write('\tКонечно он лошара')
file1.close()


file2 = open('gadji.txt','rt', encoding = 'utf-8')
text = file2.read()
file2.close()
print(text)


# file2 = open('gadji.txt','rt', encoding = 'utf-8')
# text = file2.readline()
# file2.close()
# print(text)

# file2 = open('gadji.txt','rt', encoding = 'utf-8')
# for line in file2:
# 	if not 'лошара' in line:
# 		print(line, end='')
# file2.close()

file2 = open('gadji.txt','rt', encoding = 'utf-8')
text = file2.read(9)
text2 = file2.read(9)
file2.close()
print(text, text2)

stih ='''Жил был Тина
Очень красивый мальчик
Он ел скатину
И плюхнюлся на диванчик'''

with open('stih.py','wt', encoding = 'utf-8') as f:
	f.write(stih)

