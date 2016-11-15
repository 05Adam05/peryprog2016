f1 = open('kak-vsegada.txt','wt',encoding='utf-8')
f1.write('Что либо.\n')
f1.write('Тагир любит кофе с молокм.')
print('тисак вернулся', file=f1)
f1.close()

f2 = open('kak-vsegada.txt','rt',encoding='utf-8')
text = f2.read()
f2.close()
print(text)

f2 = open('kak-vsegada.txt','rt',encoding='utf-8')
text = f2.readline()
f2.close()
print(text)

f2 = open('kak-vsegada.txt','rt',encoding='utf-8')
for line in f2:
    if not 'кофе' in line:
        print(line)
f2.close()

stih = """Сашитав хороший парень
дальше мат"""

with open('saga.txt','wt',encoding='utf-8') as f:
    f.write(stih)
