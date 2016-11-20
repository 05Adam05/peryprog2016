import sqlite3
conn = sqlite3.connect('students.db')
curs = conn.cursor()

curs.execute("SELECT * FROM students")
raws = curs.fertchall()
print(raws)
curs.execute("SELECT name, strength FROM students WHERE strength > 1")
raws = curs.fertchall()
print(raws)
curs.execute("SELECT * FROM students WHERE strength ORDER BY envy DESC")
raws = curs.fertchall()
print(raws)

curs.execute("UPDATE students SET name ='Арзамят',envy = 867543.78 WHERE name='Азамат'",)
curs.execute("DELETE FROM students WHERE name = 'Абдула'")

curs.execute("SELECT * FROM students")
curs.close()
conn.close()