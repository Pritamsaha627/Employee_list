import sqlite3
db = sqlite3.connect("employee_list.db")
cr = db.cursor()
cr.execute('create table ins(insert_by text,mobile text NOT NULL PRIMARY KEY UNIQUE ,email text NOT NULL ,salary text NOT NULL,edit_by text)')
db.commit()
db.close()