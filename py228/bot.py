import sqlite3

def create_table():
#     curs.execute("""CREATE TABLE questions
#     (type VARCHAR(50),
#     question VARCHAR(200))""")

#     ins = "INSERT INTO questions VALUES (?,?)"
#     curs.execute(ins,('food','Че ты любишь есть вообще?'))
#     curs.execute(ins,('sleep','Во сколько ты ложишься спать?'))   
#     curs.execute(ins,('stupid','Ты тупой?'))
#     curs.execute(ins,('brother','У тебя есть брат?'))

#     curs.execute("""CREATE TABLE friends
# (name VARCHAR(50),
# food VARCHAR(50),
# sleep VARCHAR(50),
# stupid VARCHAR(50),
# brother VARCHAR(50))""")

    curs.execute("INSERT INTO friends VALUES('Пацан','хинкал','во время','да','да')")
    conn.commit()


def friends(name):
    return True

def show_information(name):
   curs.execute("SELECT * FROM friends WHERE name = ?",(name,))
   raws = curs.fetchall()
   print(raws)
   print("Я знаю о тебе все.Ты любишь есть{0[1]}.Ты ложишься спать в {0[2]}. Ты тупой:{0[3]}. У тебя есть брат {0[4]} ".format(raws[0]))

def add_friends(name):
    pass

conn = sqlite3.connect('bot.db')
curs = conn.cursor()
create_table()
print('Cалам алейкум меня зовут Абдула.А тебя?')
name = input()
if friends(name):
    show_information(name)
else:
    add_friends(name)


curs.close()
conn.close()