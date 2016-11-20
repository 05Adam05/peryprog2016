import sqlite3
def create_db():
    curs.execute("""CREATE TABLE IF NOT EXISTS questions
    (type VARCHAR(50) PRIMARY KEY,
    question VARCHAR(250))""")
    ins = "INSERT OR REPLACE INTO questions VALUES(?, ?)"
    curs.execute(ins,('shmot','За шмот поясни?'))
    curs.execute(ins,('age','Сколько тебе есть?'))
    curs.execute(ins,('children','Цп есть?'))
    curs.execute(ins,('location','Откуда ты?'))
    curs.execute("""CREATE TABLE IF NOT EXISTS peoples
    (name VARCHAR(50) PRIMARY KEY,
    shmot VARCHAR(50),
    age VARCHAR(50),
    children VARCHAR(50),
    location VARCHAR(50))""")
    curs.execute("INSERT OR REPLACE INTO peoples VALUES('Расул','да','да','да','да')")
    conn.commit()
def know_you(name):
    curs.execute("SELECT name FROM peoples WHERE name = ?",(name,))
    raws = curs.fetchall()
    for raw in raws:
        if name in raw:
            print(1)
            return True
        else:
            print(2)
            return False
def show_info(name):
    curs.execute("SELECT * FROM peoples WHERE name = ?",(name,))
    raws = curs.fetchall()
    print("Я о тебе все знаю. Ты за шмот {0[1]}. Тебе лет {0[2]}. У тебя есть цп {0[3]}. Ты из {0[4]}".format(raws[0]))
def add_man(name):
    pass
conn = sqlite3.connect('pahan.db')
curs = conn.cursor()
create_db()
print("Я пахан? А ты?")
name = input()
if know_you(name):
    show_info(name)
else:
    add_man(name)
curs.close()
conn.close()