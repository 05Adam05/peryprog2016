import sqlite3
conn = sqlite3.connect('students.db')
curs = conn.cursor()
# curs.execute('DROP TABLE students')
# curs.execute("""CREATE TABLE students 
# (name VARCHAR(50) PRIMARY KEY,
# strenge INT,
# envy REAL)""")

curs.execute("INSERT INTO students VALUES('Абдула',0,12.3)")
curs.execute("INSERT INTO students VALUES('Барякят',1,2.5)")
curs.execute("INSERT INTO students VALUES('Тина' ,24,10.2 )")
name, strenge,envy = 'Азамат', -2,9.9999
curs.execute("INSERT INTO students VALUES(?,?,?)",(name, strenge, envy))
ins = "INSERT INTO students VALUES(?,?,?)"
curs.execute(ins,('Тина',1000,25.6))
conn.commit()
curs.close()
conn.close()
