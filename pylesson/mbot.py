import sqlite3
class Mbot:
    def __init__(self):
        self.conn = sqlite3.connect('mbot.db')
        self.curs = self.conn.cursor()
    def __del__(self):
        self.curs.close()
        self.conn.close()
        print('Конец')

    def give_questions(self):
        curs = self.curs
        ins = 'INSERT OR REPLACE INTO questions (type, question) VALUES(?, ?)'
        curs.execute(ins,('surname','А фамилия какая?'))
        curs.execute(ins,('nickname','Какая у тебя кликуха?'))
        curs.execute(ins,('age','Хочу знать, сколько тебе лет?'))
        curs.execute(ins,('place','Откуда сам?'))
        curs.execute(ins,('food','Любимая еда?'))
        curs.execute(ins,('color','Любимый цвет?'))
        curs.execute(ins,('life','И последний вопрос - кто ты по жизни?'))
        self.conn.commit()

    def add_friend(self, name, surname, nickname, age, place, food, color, life):
        ins = 'INSERT OR REPLACE INTO friends (name, surname, nickname, age, place, food, color, life) VALUES(?, ?, ?, ?, ?, ?, ? ,? )'
        self.curs.execute(ins,(name, surname, nickname, age, place, food, color, life))
        self.conn.commit()

    def create_tables(self):
        self.curs.execute('''CREATE TABLE IF NOT EXISTS questions
        (type VARCHAR(50) PRIMARY KEY,
        question VARCHAR(200))''')
        self.give_questions()

        # self.curs.execute('''DROP TABLE friends''')
        self.curs.execute('''CREATE TABLE IF NOT EXISTS friends
        (name VARCHAR(50) PRIMARY KEY,
        surname VARCHAR(50),
        nickname VARCHAR(50),
        age VARCHAR(50),
        place VARCHAR(50),
        food VARCHAR(50),
        color VARCHAR(50),
        life VARCHAR(50))''')
        self.add_friend('Мухаммад','Мухаммадов','Резкий','28','Хас','хинкал','черный','красавчик')

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
        name = input('Салам, меня зовут Мухамад. А тебя? ')
        if name in self.give_names():
            self.about_you(name)
        else:
            self.ask_questions(name)

m = Mbot()
m.create_tables()
m.start_chat()
