import sqlite3
db = sqlite3.connect("employee_list.db")
cr = db.cursor()
cr.execute('create table register(emp_id text NOT NULL PRIMARY KEY UNIQUE , name text NOT NULL ,password text NOT NULL)')
db.commit()
db.close()