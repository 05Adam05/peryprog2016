import sqlite3
from collections import OrderedDict
DI = OrderedDict({
   "surname":"А фамилия какая?",
   "nickname":"Какая у тебя кликуха?",
   "age":"Хочу знать: сколько тебе лет?",
   "place":"Откуда сам?",
   "food":"Любимая еда?",
   "color":"Любимый цвет?",
   "life":"И последний вопрос - кто ты по жизни?"
})
class Mbot:
    def __init__(self,name):
        self.conn = sqlite3.connect('mbot2.db')
        self.curs = self.conn.cursor()
        self.name = name
    def __del__(self):
        self.curs.close()
        self.conn.close()
        print('Конец')

    def give_questions(self,di):
        curs = self.curs
        ins = 'INSERT OR REPLACE INTO questions (type, question) VALUES(?, ?)'
        for key, value in di.items():
            curs.execute(ins,(key,value))
        self.conn.commit()

    def add_friend(self, name, surname, nickname, age, place, food, color, life):
        ins = 'INSERT OR REPLACE INTO friends (name, surname, nickname, age, place, food, color, life) VALUES(?, ?, ?, ?, ?, ?, ? ,? )'
        self.curs.execute(ins,(name, surname, nickname, age, place, food, color, life))
        self.conn.commit()

    def create_tables(self):
        self.curs.execute('''DROP TABLE friends''')
        self.curs.execute('''CREATE TABLE IF NOT EXISTS questions
        (type VARCHAR(50) PRIMARY KEY,
        question VARCHAR(200))''')
        self.give_questions(DI)
        raws = self.curs.execute('SELECT * FROM questions')
        s = "CREATE TABLE IF NOT EXISTS friends (name VARCHAR(50) PRIMARY KEY,"
        for raw in raws:
            m = "{0} VARCHAR(50),".format(raw[0])
            s += m
        s = s[:-1] +')'
        # self.curs.execute('''DROP TABLE friends''')
        self.curs.execute(s)
        # self.curs.execute('''DROP TABLE friends''')
        # self.curs.execute('''CREATE TABLE IF NOT EXISTS friends
        # (name VARCHAR(50) PRIMARY KEY,
        # surname VARCHAR(50),
        # nickname VARCHAR(50),
        # age VARCHAR(50),
        # place VARCHAR(50),
        # food VARCHAR(50),
        # color VARCHAR(50),
        # life VARCHAR(50))''')

        self.add_friend(self.name,'Мухаммадов','Резкий','28','Хас','хинкал','черный','красавчик')

    def give_names(self):
        self.curs.execute('SELECT name FROM friends')
        raws = self.curs.fetchall()
        self.names = [name[0] for name in raws]
        print(self.names)
        return self.names

    def ask_questions(self,name):
        print('Рад знакомству,',name)
        raws = self.curs.execute('SELECT * FROM questions')
        data = []
        for raw in raws:
            print(raw[1])
            n = input()
            data.append(n)
        self.add_friend(name,*data)

    def about_you(self,name):
        print('О, это ты. Я все про тебя знаю')
        self.curs.execute('SELECT * FROM friends WHERE name = ?',(name,))
        raws = self.curs.fetchone()
        print('Твоя фамилия {0[1]}. Все тебя называют {0[2]}. твой возраст {0[3]} Ты из {0[4]}.\
Любишь покушать {0[5]}. Твой любимый цвет {0[6]}. И по жизни ты {0[7]}'.format(raws))
           

    def start_chat(self):
        name = input('Салам, меня зовут {0.name}. А тебя? '.format(self))
        if name in self.give_names():
            self.about_you(name)
        else:
            self.ask_questions(name)

m = Mbot('Магаша')
m.create_tables()
m.start_chat()
