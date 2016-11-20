import sqlite3

conn = sqlite3.connect('zooshop.db')
curs = conn.cursor()


# curs.execute('''CREATE TABLE zoo
# (name VARCHAR(50) PRIMARY KEY, 
# count INT,
# cost REAL)''')

# curs.execute("INSERT INTO zoo VALUES('Джордж',1,50.80)")
# curs.execute("INSERT INTO zoo VALUES('Ленивец',1,200.80)")
# name, count, cost = 'Крипер',2,7000.10
# curs.execute("INSERT INTO zoo VALUES(?,?,?)",(name, count, cost))
# ins = "INSERT INTO zoo VALUES(?,?,?)"
# curs.execute(ins,('Страус',10,100.30))
# curs.execute(ins,('Кошка или собака. Котопес! ВО!',1,6000.5))
# curs.execute(ins,('Ифрит',4000,2500.10))
# conn.commit()

curs.execute("SELECT * FROM zoo")
raws = curs.fetchall()
print(raws)
curs.execute("SELECT name, count FROM zoo")
raws = curs.fetchall()
print(raws)
curs.execute("SELECT * FROM zoo ORDER BY cost")
raws = curs.fetchall()
print(raws)
curs.execute("SELECT * FROM zoo ORDER BY cost DESC")
raws = curs.fetchall()
print(raws)
curs.execute("SELECT * FROM zoo WHERE cost > 200 ORDER BY cost")
raws = curs.fetchall()
print(raws)
curs.execute("UPDATE zoo SET name = 'Гаст', cost = 4000.20 WHERE name = 'Джордж'")
curs.execute("DELETE FROM zoo WHERE name = 'Страус'")
curs.execute("SELECT * FROM zoo")
raws = curs.fetchall()
print(raws)